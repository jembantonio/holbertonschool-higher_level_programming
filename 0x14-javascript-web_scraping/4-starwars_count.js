#!/usr/bin/node

const request = require('request');

const query = 'http://swapi.co/api/films/';

request(query, function (err, r, data) {
  if (!err) {
    let count = 0;
    const titles = JSON.parse(data).results;
    for (const title in titles) {
      const characters = titles[title].characters;
      for (const character in characters) {
        if (characters[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(err);
  }
});
