#!/usr/bin/node

// Include process module
const process = require('process');

// Printing process.argv property value
const args = process.argv;

// The number
const pssdArg1 = parseInt(args[2]);
const pssdArg2 = parseInt(args[3]);

// Returns a + b
function add (a, b) {
  return a + b;
}

// Print result
console.log(add(pssdArg1, pssdArg2));
