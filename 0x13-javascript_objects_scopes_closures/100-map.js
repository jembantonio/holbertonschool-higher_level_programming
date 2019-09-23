#!/usr/bin/node
const list = require('./100-data.js').list;

const newL = list.map(function (x, i) {
    return x * i;
});
console.log(list);
console.log(newL);
