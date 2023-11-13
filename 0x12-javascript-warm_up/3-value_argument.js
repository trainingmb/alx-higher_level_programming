#!/usr/bin/node

// Include process module
const process = require('process');

// Printing process.argv property value
const args = process.argv;

// No arguments
if (args[2] == null) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
