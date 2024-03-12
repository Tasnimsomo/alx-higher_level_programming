#!/usr/bin/node
exports.converter = function (base) {
	function convert (number) {
		if (n < base) return n.tostring(base)
		else {
			return convert(Math.floor(number / base)) + (number % base).tostring(base);
		}
		return convert;
	};
