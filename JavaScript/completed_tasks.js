#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todosData = JSON.parse(body);

    const completedTasks = {};
    todosData.forEach((todo) => {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
	  completedTasks[todo.userId]++;
	} else {
	  completedTasks[todo.userId] = 1;
	}
      }
    });

    console.log(JSON.stringify(completedTasks, null, 2));
  }
});
