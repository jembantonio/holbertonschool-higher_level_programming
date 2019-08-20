#!/bin/bash
# takes a URL, sends a GET response and displays the body
curl -sI GET "$1"
