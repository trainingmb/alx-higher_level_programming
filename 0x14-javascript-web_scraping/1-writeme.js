#!/usr/bin/node

// For handling arguments and files
const process = require('process');
const fs = require('fs');

// Arguments variable
const args = process.argv;

// Argument provided
if (args[3] != null) {
  fs.writeFile(args[2], args[3], err => {
    if (err) {
      console.error(err);
      return;
    }
  });
}
