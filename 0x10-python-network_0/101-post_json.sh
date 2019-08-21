#!/bin/bash
#sends a JSON POST request to a URL and displays the body
curl -H "Content-Type: application/json" -s "$1" -X POST -d "@$2"
