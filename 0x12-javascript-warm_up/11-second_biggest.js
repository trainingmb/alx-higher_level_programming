#!/usr/bin/node

// Include process module
const process = require('process');

// Printing process.argv property value
const args = process.argv;

// The number
let l1 = 0;
let l2 = 0;
let i = 4;
let cur = 0;

// Length of 3
if (args.length > 3) {
  l1 = parseInt(args[2]);
  l2 = parseInt(args[3]);
  if (l2 > l1) {
    cur = l2;
    l2 = l1;
    l1 = cur;
  }
  while (i < args.length) {
    cur = parseInt(args[i]);
    if (cur > l1) {
      l2 = l1;
      l1 = cur;
    } else if (cur < l1 && cur > l2) {
      l2 = cur;
    }
    i++;
  }
}

console.log(l2);
