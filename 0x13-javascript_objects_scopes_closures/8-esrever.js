#!/usr/bin/node

exports.esrever = function (list) {
  let x = list.length - 1;
  const reved = [];
  while (x >= 0) {
    reved.push(list[x]);
    x -= 1;
  }
  return reved;
};

