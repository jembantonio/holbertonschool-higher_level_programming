#!/usr/bin/node

if (process.argv.slice(2).length < 2) {
  console.log(0)
} else {
  console.log(process.argv.slice(2).sort((a, b) => b - a)[1]);
}
