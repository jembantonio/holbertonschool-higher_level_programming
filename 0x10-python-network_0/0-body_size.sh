#!/bin/bash
# takes a url as an argument and displays the size of the body
curl -sI $1 | grep Content-Length | cut -f 2 -d ':'
