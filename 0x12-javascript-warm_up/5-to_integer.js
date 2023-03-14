#!/usr/bin/node
const input = process.argv[2];
const num = parseInt(input);

if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
