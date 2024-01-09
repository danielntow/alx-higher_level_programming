#!/usr/bin/node

const OldSquare = require('./5-square.js');

class Square extends OldSquare {
  charPrint (c = 'X') {
    const line = c.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }
}

module.exports = Square;
