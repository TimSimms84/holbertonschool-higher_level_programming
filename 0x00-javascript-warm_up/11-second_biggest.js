#!/usr/bin/node

const a = process.argv.slice(2);
let maxNumber = 0;
if (process.argv.length > 3) {
  a.sort();
  maxNumber = Number(a[a.length - 2]);
}
console.log(maxNumber);
