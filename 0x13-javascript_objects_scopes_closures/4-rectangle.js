#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    console.log((('X'.repeat(this.width) + '\n').repeat(this.height)).slice(0, -1));
  }
  double() {
    this.width *= 2;
    this.height *= 2;
  }
  rotate() {
    let temp = this.width;
    this.width =  this.height;
    this.height = temp;
  }
};
