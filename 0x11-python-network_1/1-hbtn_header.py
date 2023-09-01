#!/usr/bin/python3
""" This module sends a request to X-Request-Id"""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    page = request.Request(url)
    with request.urlopen(page) as response:
        print(dict(response.headers).get("X-Request-Id"))
