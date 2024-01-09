#!/usr/bin/node

const { dict } = require('./101-data');

const usersByOccurrence = {};
Object.keys(dict).forEach((userId) => {
  const occurrence = dict[userId];
  if (!usersByOccurrence[occurrence]) {
    usersByOccurrence[occurrence] = [];
  }
  usersByOccurrence[occurrence].push(userId);
});

console.log(usersByOccurrence);
