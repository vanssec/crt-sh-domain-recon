import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import ijson
import time
import sys

def fetch_name_values(domain):
    """
    Fetch all name_value entries from crt.sh for a given domain.
    Retries on 404/429/5xx, includes wildcards, handles slow responses.
    """
    url = f"https://crt.sh/?q={domain}&output=json"
    print(f"Querying URL: {url}")
    
    # Configure retry strategy
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=10, status_forcelist=[404, 429, 500, 502, 503, 504])
    session.mount('https://', HTTPAdapter(max_retries=retries))
    
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        attempts += 1
        print(f"Attempt {attempts}/{max_attempts} for {domain}", end="", flush=True)
        
        try:
            # Fetch with 60s timeout, stream for large responses
            response = session.get(url, timeout=60, stream=True)
            response.raise_for_status()
            
            # Clear progress line
            print("\r" + " " * 50 + "\r", end="", flush=True)
            
            # Parse JSON incrementally with ijson
            name_values = set()
            try:
                parser = ijson.items(response.raw, 'item')
                for entry in parser:
                    name_value = entry.get('name_value', '')
                    domains = name_value.split('\n')
                    for domain in domains:
                        domain = domain.strip()
                        if domain:
                            name_values.add(domain)
            
            except ijson.JSONError as e:
                print(f"\rError: Failed to parse JSON response: {e}")
                return [], f"JSON parse error: {e}", response.status_code, attempts
            
            return sorted(list(name_values)), None, response.status_code, attempts
        
        except requests.exceptions.Timeout:
            error_msg = f"Timed out after 60 seconds (attempt {attempts}/{max_attempts})"
            print(f"\rError: {error_msg}")
            if attempts == max_attempts:
                return [], error_msg, None, attempts
            time.sleep(10)  # Wait before retry
            print("\r" + " " * 50 + "\r", end="", flush=True)
        
        except requests.exceptions.HTTPError as e:
            error_msg = f"HTTP error: {e} (status code: {e.response.status_code}, attempt {attempts}/{max_attempts})"
            print(f"\rError: {error_msg}")
            if attempts == max_attempts:
                return [], error_msg, e.response.status_code if e.response else None, attempts
            time.sleep(10)  # Wait before retry
            print("\r" + " " * 50 + "\r", end="", flush=True)
        
        except requests.exceptions.RequestException as e:
            error_msg = f"Network error: {e} (attempt {attempts}/{max_attempts})"
            print(f"\rError: {error_msg}")
            if attempts == max_attempts:
                return [], error_msg, None, attempts
            time.sleep(10)  # Wait before retry
            print("\r" + " " * 50 + "\r", end="", flush=True)
    
    return [], "Max retry attempts reached", None, attempts

def main():
    domain = input("Enter the domain (e.g., example.com): ").strip()
    if not domain:
        print("Error: No domain provided")
        return
    
    print(f"Fetching name_value entries for {domain} from crt.sh...")
    start_time = time.time()
    
    name_values, error, status_code, attempts = fetch_name_values(domain)
    
    elapsed_time = time.time() - start_time
    if name_values:
        print(f"\nFound {len(name_values)} unique name_value entries for {domain}:")
        with open(f"name_values_{domain}.txt", "w") as f:
            for value in name_values:
                print(value)
                f.write(f"{value}\n")
        print(f"\nResults saved to name_values_{domain}.txt")
    else:
        print(f"\nNo name_value entries found for {domain}")
        if error:
            print(f"Reason: {error}")
        if status_code:
            print(f"Status Code: {status_code}")
    
    print(f"Attempts: {attempts}")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print("\nNote: If you see a dependency warning, update requests: `pip install --upgrade requests urllib3 chardet`")

if __name__ == "__main__":
    main()
