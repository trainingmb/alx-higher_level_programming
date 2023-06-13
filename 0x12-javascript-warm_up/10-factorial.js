#!/usr/bin/node

// Include process module
const process = require('process');

// Printing process.argv property value
const args = process.argv;

// The number
const pssdArg1 = parseInt(args[2]);

// Factorial Function
function fac (i) {
  if (isNaN(i) || i < 2) {
    return 1;
  } else {
    return i * fac(i - 1);
  }
}

console.log(fac(pssdArg1));
