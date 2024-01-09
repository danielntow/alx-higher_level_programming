#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (!w || !h || w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      // Create an empty object
      return;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
