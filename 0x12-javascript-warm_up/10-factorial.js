#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n === Infinity) {
    return 1;
  } else if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(Number(process.argv[2])));
