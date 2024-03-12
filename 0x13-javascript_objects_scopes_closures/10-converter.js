#!/usr/bin/node
exports.converter = function (base) {
  function convert (number) {
    if (number === 0) return '';

    return convert(Math.floor(number / base)) + (number % base);
  }
  return convert;
};
