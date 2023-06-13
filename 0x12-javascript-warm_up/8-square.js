#!/usr/bin/node

// Include process module
const process = require('process');

// Printing process.argv property value
const args = process.argv;

// The number
const pssdArg = parseInt(args[2]);
let sq = '';

// Print two arguments
if (isNaN(pssdArg)) {
  console.log('Missing size');
} else {
  let i = 0;

  while (i < pssdArg) {
    sq += 'X';
    i++;
  }
  i = 0;

  while (i < pssdArg) {
    console.log(sq);
    i++;
  }
}
