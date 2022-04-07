#!/usr/bin/node

const fileServer = require('fs');
const file = process.argv[2];
fileServer.readFile(file, 'utf-8', function (error, content) {
  if (error) {
    console.error(error);
  } else {
    console.log(content);
  }
});
