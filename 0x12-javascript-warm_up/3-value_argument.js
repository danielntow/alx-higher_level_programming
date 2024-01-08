#!/usr/bin/node

// Get the first argument from process.argv
const arg = process.argv[2];

// Check if an argument is provided and print accordingly
if (!arg) {
  console.log('No argument');
} else {
  console.log(arg);
}
