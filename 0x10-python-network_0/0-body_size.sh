#!/bin/bash
# a bash script that takes in URL and dislay the size of the body of the response.
curl -s "$1" | wc -c
