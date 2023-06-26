#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0) {
      this.width = w;
    }
    if (Number.isInteger(h) && h > 0) {
      this.height = h;
    }
  }
};
