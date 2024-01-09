#!/usr/bin/node

function add (a, b) {
  return a + b;
}

module.exports.add = add; // Making the function visible from outside
