#!/usr/bin/node

let person = {
  name: 'Alice',
  age: 25,
  email: 'alice@example.com'
};

// Iterating over object properties using for...in loop
for (let key in person) {
  console.log(`${key}: ${person[key]}`);
}

// Using Object.keys() to get an array of object keys
let keys = Object.keys(person);
console.log(keys); // Output: ['name', 'age', 'email']

// Using Object.values() to get an array of object values
let values = Object.values(person);
console.log(values); // Output: ['Alice', 25, 'alice@example.com']

// Using Object.entries() to get an array of key-value pairs
let entries = Object.entries(person);
console.log(entries); // Output: [['name', 'Alice'], ['age', 25], ['email', 'alice@example.com']]
