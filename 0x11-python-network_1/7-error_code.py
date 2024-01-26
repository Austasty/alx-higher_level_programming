#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    rd = requests.get(url)
    if rd.status_code >= 400:
        print("Error code: {}".format(rd.status_code))
    else:
        print(rd.text)
