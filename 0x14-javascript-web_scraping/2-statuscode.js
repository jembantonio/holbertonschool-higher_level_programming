#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, r) {
  if (!err) {
    console.log('code: ' + r.statusCode);
  } else {
    console.log(err);
  }
});
