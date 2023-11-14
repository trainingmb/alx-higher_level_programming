#!/usr/bin/node
const Sqr = require('./5-square');

module.exports = class Square extends Sqr {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      console.log(((c.repeat(this.width) + '\n').repeat(this.height)).slice(0, -1));
    }
  }
};
