#!/bin/bash

curl -s -w "\nHTTP Status Code: %{http_code}\n" "$1" | awk '/HTTP Status Code: 200/ {flag=1; next} flag;'
