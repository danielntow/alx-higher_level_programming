#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);

    // Filter completed tasks
    const completedTasks = todos.filter(task => task.completed);

    // Count completed tasks for each user
    const completedTasksByUser = completedTasks.reduce((acc, task) => {
      acc[task.userId] = (acc[task.userId] || 0) + 1;
      return acc;
    }, {});

    console.log(completedTasksByUser);
  }
});
