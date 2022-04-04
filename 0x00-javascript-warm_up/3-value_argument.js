#!/usr/bin/node
const argvLength = process.argv.length;
const argvContent = process.argv[2];
if (argvLength === 2) {
  console.log('No argument');
} else if (argvLength === 3) {
  console.log(argvContent);
}
