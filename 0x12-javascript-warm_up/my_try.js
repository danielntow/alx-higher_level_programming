#!/usr/bin/node

// Constructor function for creating Person objects
function Person (name) {
  this.name = name;
}

// Adding a method to the Person prototype
Person.prototype.greet = function () {
  return `Hello, my name is ${this.name}!`;
};

// Creating objects using the constructor
let person1 = new Person('Alice');
let person2 = new Person('Bob');

console.log(person1.greet()); // Output: 'Hello, my name is Alice!'
console.log(person2.greet()); // Output: 'Hello, my name is Bob!'

function Person (name) {
  this.name = name;
}

// Adding a method to the Person prototype
Person.prototype.greet = function () {
  return `Hello, my name is ${this.name}!`;
};

let person = new Person('Alice');

console.log(person.greet()); // Output: 'Hello, my name is Alice!'
// --------------------------------------------------------------------------------
// Parent constructor function
function Animal (type) {
  this.type = type;
}

// Adding a method to the Animal prototype
Animal.prototype.sound = function () {
  return 'Making a sound...';
};

// Child constructor function inheriting from Animal
function Dog (type, breed) {
  Animal.call(this, type);
  this.breed = breed;
}

// Inheriting the prototype methods
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

// Adding a method specific to Dog
Dog.prototype.bark = function () {
  return 'Barking!';
};

// Creating instances
let animal = new Animal('Generic');
let dog = new Dog('Canine', 'Labrador');

console.log(animal.sound()); // Output: 'Making a sound...'
console.log(dog.sound()); // Output: 'Making a sound...'
console.log(dog.bark()); // Output: 'Barking!'
