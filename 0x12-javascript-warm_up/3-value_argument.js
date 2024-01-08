#!/usr/bin/node
const numArgs = process.argv;

if (numArgs[2]) {
  console.log(numArgs[2]);
} else {
  console.log('No argument');
}
