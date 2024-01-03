#!/usr/bin/node

// For handling arguments and request
const process = require('process');
const request = require('request');

// Arguments variable
const args = process.argv;

// Argument provided
if (args[2] != null) {
  const url = 'https://swapi-api.alx-tools.com/api/films/';
  request(url + args[2], function (err, response, body) {
    if (!err && response.statusCode === 200) {
      const info = JSON.parse(body);
      console.log(info.title);
    }
  });
}
