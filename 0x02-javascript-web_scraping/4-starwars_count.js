#!/usr/bin/node

const request = require('request');
const website = process.argv[2];
request(website, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const jsonReturn = JSON.parse(body).results;
    let wedgeApperance = 0;
    for (const movies in jsonReturn) {
      const characters = jsonReturn[movies].characters;
      for (const charIndex in characters) {
        if (characters[charIndex].includes('/18/')) {
          wedgeApperance += 1;
        }
      }
    }
    console.log(wedgeApperance);
  }
});
