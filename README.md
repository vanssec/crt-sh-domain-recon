CRT.sh Domain Name Fetcher

A Python script to fetch and save name_value entries for a given domain from crt.sh, handling retries, timeouts, and large JSON responses efficiently.

Features

- Fetches subdomains and related domains from crt.sh using the provided domain query.
- Handles errors gracefully:
  - Retries on HTTP errors (404, 429, 5xx) with a backoff strategy.
  - Manages timeouts and network issues with up to 5 retry attempts.
- Processes large responses using streaming and incremental JSON parsing with ijson.
- Saves results to a text file (name_values_<domain>.txt) for easy access.
- User-friendly output with progress, error messages, and execution time.

Requirements

- Python 3.6+
- Required packages:
  - requests
  - ijson
  - urllib3 (for retry logic)

Install dependencies using:
pip install requests ijson urllib3

To ensure compatibility, update dependencies if needed:
pip install --upgrade requests urllib3 chardet

Usage

1. Clone or download the script.
2. Run the script and provide a domain when prompted:
python main.py

3. Enter a domain (e.g., example.com) when prompted.
4. The script will:
   - Query crt.sh for name_value entries.
   - Display progress and any errors.
   - Save unique entries to name_values_<domain>.txt.
   - Show the number of entries found, attempts made, and time taken.

Example

$ python crtsh_fetcher.py
Enter the domain (e.g., example.com): example.com
Fetching name_value entries for example.com from crt.sh...
Attempt 1/5 for example.com
Found 10 unique name_value entries for example.com:
sub1.example.com
sub2.example.com
...
Results saved to name_values_example.com.txt
Attempts: 1
Time taken: 2.34 seconds

Code Overview

- Main Function: Prompts for a domain and orchestrates the fetching process.
- Fetch Function (fetch_name_values):
  - Queries crt.sh with a 60-second timeout.
  - Uses requests.Session with a retry strategy for robustness.
  - Parses JSON incrementally with ijson to handle large responses.
  - Returns sorted unique domains, error message (if any), status code, and attempts made.
- Error Handling:
  - Retries on 404, 429, and 5xx errors with a 10-second backoff.
  - Catches timeouts and network errors.
  - Reports JSON parsing issues.
- Output:
  - Saves results to a text file.
  - Prints progress, results, and diagnostics (attempts, time taken).

Notes

- Rate Limiting: crt.sh may impose rate limits, triggering 429 errors. The script retries with a backoff to mitigate this.
- Tip: Use a specific domain (e.g., example.com) to avoid overly broad queries that may take longer or hit rate limits.
- Caution: Ensure requests, ijson, and urllib3 are up-to-date to avoid compatibility issues.
- Large Responses: Streaming and incremental parsing prevent memory issues with large JSON responses.
- Output File: Results are saved as name_values_<domain>.txt in the script's directory.
