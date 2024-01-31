#!/bin/bash
# Sends a request to a URL and displays only the status code of the response
url="$1" status_code=$(curl -s -o /dev/null -w "%{http_code}" "$url") && echo "$status_code"
