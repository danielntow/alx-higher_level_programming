#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const newFunc = (a, b) => {
  return a + b;
};

const checkFunc = function (a, b) {
  return result;
};

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

const result = newFunc(arg1, arg2);
console.log(result);
