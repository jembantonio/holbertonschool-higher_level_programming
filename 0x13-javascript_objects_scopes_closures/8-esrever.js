#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  const length = list.length - 1;
  for (let i = length; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
