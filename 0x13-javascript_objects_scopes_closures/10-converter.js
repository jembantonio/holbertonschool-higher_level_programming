#!/usr/bin/node

exports.converter = function (base) {
  return function baseval (num) {
    return num.toString(base);
  };
};
