#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase (n) {
    if (n < base) {
      return n.toString(base);
    } else {
      return convertToBase(Math.floor(n / base)) + (n % base).toString(base);
    }
  };
};
