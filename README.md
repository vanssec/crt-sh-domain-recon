# CRT.sh Domain Name Grabber

This Python script grabs domain names (like `*.example.com`) from [crt.sh](https://crt.sh) for any domain you type in. It saves them to a text file and handles problems like bad internet or slow servers.

## Features
- Pulls domain names from **crt.sh** SSL certificates.
- Tries **5 times** if the server fails.
- Saves results to `name_values_<yourdomain>.txt`.
- Shows errors and how long it takes.

## Requirements
- Python **3.6** or newer.
- Install these packages:
  ```bash
  pip install requests ijson urllib3
Installation

Clone the repo:
bashgit clone https://github.com/yourusername/crtsh-domain-grabber.git
cd crtsh-domain-grabber

Install packages:
bashpip install requests ijson urllib3


Usage

Run the script:
bashpython script.py

Type a domain (like example.com).
Check name_values_<yourdomain>.txt for results.

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

Package warnings? Update them:
bashpip install --upgrade requests urllib3

No results? Check your internet or if crt.sh is down.
Retries wait 10 seconds if something fails.

Limitations

Needs crt.sh to be online.
Big domain lists might take a bit.

Contributing
Got ideas? Fork the repo, make changes, and send a pull request!
License
Licensed under the MIT License.
