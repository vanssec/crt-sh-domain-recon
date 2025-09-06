# CRT.sh Domain Name Grabber

This Python script grabs domain names (like `*.example.com`) from **[crt.sh](https://crt.sh)** for any domain you enter. It saves them to a text file and handles issues like bad internet or slow servers.

## Features
- Pulls domain names from **crt.sh** SSL certificates.
- Retries **5 times** if the server fails or times out.
- Saves results to `name_values_<yourdomain>.txt`.
- Shows errors and how long it takes in **seconds**.

## Requirements
- **Python 3.6** or newer.
- Install these packages:
  ```bash
  pip install requests ijson urllib3
Installation

Clone the repository:
bashgit clone https://github.com/yourusername/crtsh-domain-grabber.git

Navigate to the project folder:
bashcd crtsh-domain-grabber

Install required packages:
bashpip install requests ijson urllib3


Usage

Run the script:
bashpython script.py

Enter a domain (e.g., example.com) when prompted.
Check the output file name_values_<yourdomain>.txt for results.

Example
bash$ python script.py
Enter the domain (e.g., example.com): example.com
Fetching domain names for example.com from crt.sh...
Found 5 domains:
example.com
www.example.com
...
Saved to name_values_example.com.txt
Time taken: 1.2 seconds
Troubleshooting

See package warnings? Update them:
bashpip install --upgrade requests urllib3

No results? Check your internet or if crt.sh is down.
The script waits 10 seconds between retries if something fails.

Limitations

Requires crt.sh to be online.
Large domain lists may take a few seconds to process.

Contributing
Want to help? Fork the repo, make changes, and submit a pull request!
License
Licensed under the MIT License.
