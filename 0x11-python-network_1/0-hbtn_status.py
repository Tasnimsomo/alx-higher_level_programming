#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        raw_data = response.read()

    decoded_data = raw_data.decode("utf-8")

    print("Body response:")
    print("\t- type:", type(raw_data))
    print("\t- content:", raw_data)
    print("\t- utf8 content:", decoded_data)
