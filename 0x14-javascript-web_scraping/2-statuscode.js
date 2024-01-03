#!/usr/bin/node

// For handling arguments and request
const process = require('process');
const request = require('request');

// Arguments variable
const args = process.argv;

// Argument provided
if (args[2] != null) {
  request(args[2], function(err, response, body) {
    if (!err) {
      console.log("code:", response && response.statusCode);
    }
  });
}
