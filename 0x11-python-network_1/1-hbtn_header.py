#!/usr/bin/python3
"""1. Response header value #0"""

import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        id_request = response.getheader('X-Request-Id')
    print(id_request)
