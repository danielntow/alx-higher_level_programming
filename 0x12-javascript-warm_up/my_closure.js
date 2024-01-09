#!/usr/bin/node

function outerFunction () {
  let outerVar = 'I am from the outer function';

  function innerFunction () {
    console.log(outerVar); // Accessing outerVar from the outer scope
  }

  return innerFunction; // Return the inner function
}

let myClosure = outerFunction(); // Assign the inner function to myClosure
myClosure(); // Execute myClosure, still able to access outerVar

function outerFunction (outerVar) {
  function innerFunction () {
    console.log(outerVar); // Accessing outerVar from the outer function's scope
  }

  return innerFunction; // Return the inner function
}

let closureA = outerFunction('Closure A');
let closureB = outerFunction('Closure B');

closureA(); // Output: 'Closure A'
closureB(); // Output: 'Closure B'

function createCounter () {
  let count = 0;

  return {
    increment: function () {
      count++;
      console.log(count);
    },
    reset: function () {
      count = 0;
      console.log('Counter reset');
    }
  };
}

let counter = createCounter();
counter.increment(); // Output: 1
counter.increment(); // Output: 2
counter.reset(); // Output: 'Counter reset'
