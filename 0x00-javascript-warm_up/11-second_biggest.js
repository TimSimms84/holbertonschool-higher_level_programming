#!/usr/bin/node

const a = process.argv.slice(2);
let maxNumber = 0;

if (process.argv.length <= 3) {
  console.log('0');
} else {
  a.sort();
  maxNumber = a[a.length - 2];
  console.log(maxNumber);
}
