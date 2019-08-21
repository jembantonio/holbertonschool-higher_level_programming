#!/bin/bash
# bash script that makses a request to 0.0.0.0:5000/catch_me
# and causes the server to respond with a message "You got me!"
curl -sLX PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
