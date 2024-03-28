#!/usr/bin/python3
"""3. Error code #0"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response = response.read()
            decoded_data = response.decode("utf-8")
            print(decoded_data)

    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
