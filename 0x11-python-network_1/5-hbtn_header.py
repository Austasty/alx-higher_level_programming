#!/usr/bin/python3
"""Displays the X-Request-Id header variable request to a given URL.
Usage: ./5-hbtn_header.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    rd = requests.get(url)
    print(rd.headers.get("X-Request-Id"))
