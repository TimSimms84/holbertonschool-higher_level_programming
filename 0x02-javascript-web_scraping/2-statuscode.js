#!/usr/bin/node

const request = require('request');
const website = process.argv[2];
request(website, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
