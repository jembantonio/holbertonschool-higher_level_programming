#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], function (err, body) {
  if (err) {
    console.log(err);
  }
  body = "" + body
  console.log(body.toString('utf-8'));
});
