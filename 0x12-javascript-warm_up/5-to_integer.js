#!/usr/bin/node

// Include process module
const process = require('process');

// Printing process.argv property value
const args = process.argv;

// An integer
if (isNaN(parseInt(args[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[2]));
}
