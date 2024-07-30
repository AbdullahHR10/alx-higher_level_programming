#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const tasksCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 0;
      }
      tasksCompleted[todo.userId]++;
    }
  });
  console.log(tasksCompleted);
});
