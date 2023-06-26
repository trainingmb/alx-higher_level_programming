#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.height = h;
      this.width = w;
    }
  }
};
