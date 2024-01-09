#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof w !== 'number' || typeof h !== 'number') {
      return {}; // Return an empty object for invalid inputs
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (Object.keys(this).length === 0) {
      return; // Empty object, do not print
    }

    const row = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}

module.exports = Rectangle;
