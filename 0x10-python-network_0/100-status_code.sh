#!/bin/bash
#sends a request to a URL and display only the stauts code
curl -s -o /dev/null -w '%{http_code}' "$1"
