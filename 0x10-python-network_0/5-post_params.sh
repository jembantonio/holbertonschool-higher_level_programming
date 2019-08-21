#!/bin/bash
# a bash script that sends a post request and dsiplays the response of URL
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
