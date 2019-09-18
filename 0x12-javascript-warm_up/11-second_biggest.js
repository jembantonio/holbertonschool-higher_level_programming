#!/usr/bin/node

var arr = process.argv.slice(2);

if (arr.length < 2) {
  console.log(0)
} else {
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
