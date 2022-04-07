#!/usr/bin/node

const fileServer = require('fs');
const file = process.argv[2];
const fileContent = process.argv[3];
fileServer.writeFile(file, fileContent, 'utf-8', function (error, content) {
  if (error) {
    console.error(error);
  }
});
