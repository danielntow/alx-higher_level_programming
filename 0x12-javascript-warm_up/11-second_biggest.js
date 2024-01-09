#!/usr/bin/node

function findSecondLargest (args) {
  const numbers = args.map(Number); // Convert arguments to numbers
  const distinctNumbers = Array.from(new Set(numbers)); // Remove duplicates

  if (distinctNumbers.length <= 1) {
    console.log(0); // If no argument or only one argument, print 0
  } else {
    distinctNumbers.sort((a, b) => b - a); // Sort numbers in descending order
    console.log(distinctNumbers[1]); // Print the second largest number
  }
}

const argumentsList = process.argv.slice(2); // Extract arguments except the script name and node command
findSecondLargest(argumentsList);
