#!/usr/bin/node

// For handling arguments and files
const process = require('process');
const fs = require('fs');
const request = require('request');

// Arguments variable
const args = process.argv;

// Argument provided
if (args[3] != null) {
  request(args[2], function (err, response, body) {
    if (!err && response.statusCode === 200) {
      fs.writeFile(args[3], body, error => {
        if (error) {
          console.error(error);
        }
      });
    }
  });
}
