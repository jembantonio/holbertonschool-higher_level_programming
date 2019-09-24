#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, r, body) {
  if (!err) {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else if (err) {
    console.log(err);
  }
});
