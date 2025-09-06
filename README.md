# CRT.sh Domain Name Fetcher

A Python script to **fetch** and **save** `name_value` entries for a given domain from [crt.sh](https://crt.sh/), handling _retries_, _timeouts_, and _large JSON responses_ efficiently.

## ✨ **Features**

- **Fetches subdomains and related domains** from crt.sh using the provided domain query.
- **Robust error handling**:
  - Retries on HTTP errors (`404`, `429`, `5xx`) with a backoff strategy.
  - Manages timeouts with up to **5 retry attempts**.
- **Optimized for large responses** using streaming and incremental JSON parsing with `ijson`.
- **Saves results** to a text file (`name_values_<domain>.txt`) for easy access.
- **User-friendly output** with progress updates, error messages, and execution time.

## 🛠 **Requirements**

- **Python 3.6+**
- Required packages:
  - `requests`
  - `ijson`
  - `urllib3` (for retry logic)

Install dependencies using:

```bash
pip install requests ijson urllib3
```

To ensure compatibility, update dependencies if needed:

```bash
pip install --upgrade requests urllib3 chardet
```

## 🚀 **Usage**

1. Clone or download the script.
2. Run the script and provide a domain when prompted:

```bash
python crtsh_fetcher.py
```

3. Enter a domain (e.g., `example.com`) when prompted.
4. The script will:
   - Query [crt.sh](https://crt.sh/) for `name_value` entries.
   - Display _progress_ and any _errors_.
   - Save unique entries to `name_values_<domain>.txt`.
   - Show the number of entries found, attempts made, and time taken.

### 📋 **Example**

```bash
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
```

## 🔍 **Code Overview**

- **Main Function**: Prompts for a domain and orchestrates the fetching process.
- **Fetch Function** (`fetch_name_values`):
  - Queries crt.sh with a **60-second timeout**.
  - Uses `requests.Session` with a retry strategy for _robustness_.
  - Parses JSON incrementally with `ijson` to handle large responses.
  - Returns sorted unique domains, error message (if any), status code, and attempts made.
- **Error Handling**:
  - Retries on `404`, `429`, and `5xx` errors with a **10-second backoff**.
  - Catches _timeouts_ and _network errors_.
  - Reports JSON parsing issues.
- **Output**:
  - Saves results to a text file.
  - Prints progress, results, and diagnostics (attempts, time taken).

## 📝 **Notes**

> [!NOTE]  
> **Rate Limiting**: crt.sh may impose rate limits, triggering `429` errors. The script retries with a backoff to mitigate this.

> [!TIP]  
> Use a specific domain (e.g., `example.com`) to avoid overly broad queries that may take longer or hit rate limits.

> [!CAUTION]  
> Ensure `requests`, `ijson`, and `urllib3` are _up-to-date_ to avoid compatibility issues.

- **Large Responses**: Streaming and incremental parsing prevent memory issues with large JSON responses.
- **Output File**: Results are saved as `name_values_<domain>.txt` in the script's directory.

## 📜 **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
