#!/usr/bin/node

const request = require('request');

const query = 'http://swapi.co/api/films/' + process.argv[2];

request(query, function (err, r, body) {
  if (!err) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log(err);
  }
});
