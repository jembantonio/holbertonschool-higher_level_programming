#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const length = list.length;
  let count = 0;
  for (let i = 0; i < length; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
