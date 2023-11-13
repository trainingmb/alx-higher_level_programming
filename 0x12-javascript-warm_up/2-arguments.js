#!/usr/bin/node

// Include process module
const process = require('process');

// Printing process.argv property value
const args = process.argv;

// No arguments
if (args.length < 3) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
