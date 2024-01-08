#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  } else if (n === 0 || n === 1) {
    return 1; // Base case: Factorial of 0 and 1 is 1
  } else {
    return n * factorial(n - 1); // Recursive call to compute factorial
  }
}

const argument = parseInt(process.argv[2]);
const result = factorial(argument);
console.log(result);
