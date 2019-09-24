#!/usr/bin/node

const fs = require('fs');
let data = process.argv[3]

fs.writeFile(process.argv[2], data, function (err) {
    if (err) {
        console.log(err);
    }
});
