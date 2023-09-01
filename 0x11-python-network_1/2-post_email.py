#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email_address = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email_address).encode("ascii")

    page = urllib.request.Request(url, data)
    with urllib.request.urlopen(page) as response:
        print(response.read().decode("utf-8"))
