#!/bin/bash
# display all the HTTP methods the server will accept using curl.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
