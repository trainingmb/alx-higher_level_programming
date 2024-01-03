#!/usr/bin/node

// For handling arguments and request
const process = require('process');
const request = require('request');

// Arguments variable
const args = process.argv;

// Argument provided
if (args[2] != null) {
  const id = '18';
  var url = 'https://swapi-api.alx-tools.com/api/people/' + id;
  let count = 0;
  request(url, function (err, response, body) {
    if (!err && response.statusCode === 200) {
      const info = JSON.parse(body);
      console.log(info.films.length);
    }
  });
}
