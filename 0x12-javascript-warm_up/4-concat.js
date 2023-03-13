#!/usr/bin/node
const [, , arg1 = 'undefined', arg2 = 'undefined'] = process.argv;
console.log(`${arg1} is ${arg2}`);
