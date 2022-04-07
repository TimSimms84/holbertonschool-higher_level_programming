#!/usr/bin/node

const request = require('request');
const website = process.argv[2];
request(website, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const completedTask = {};
    const content = JSON.parse(body);
    for (let i = 0; i < content.length; i++) {
      const id = content[i].userId;
      const completed = content[i].completed;
      if (completed) {
        if (!completedTask[id]) {
          completedTask[content[i].userId] = 1;
        } else {
          completedTask[content[i].userId] += 1;
        }
      }
    }
    console.log(completedTask);
  }
});
