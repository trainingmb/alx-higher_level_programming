#!/usr/bin/node

// Include process module
const process = require('process');

// Printing process.argv property value
const args = process.argv;

// Print two arguments
console.log(args[2] + ' is ' + args[3]);
