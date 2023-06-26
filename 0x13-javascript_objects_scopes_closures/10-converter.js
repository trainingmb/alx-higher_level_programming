#!/usr/bin/node

exports.converter = function (base) {
  function foo (num) {
    return num.toString(base);
  }
  return foo;
};
