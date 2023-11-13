#!/usr/bin/node

// Include process module
const process = require('process');

// Printing process.argv property value
const args = process.argv;

// The number
const pssdArg = parseInt(args[2]);

// Print two arguments
if (isNaN(pssdArg)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;

  while (i < pssdArg) {
    console.log('C is fun');
    i++;
  }
}
