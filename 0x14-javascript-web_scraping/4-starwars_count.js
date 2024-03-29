#!/usr/bin/node

// For handling arguments and request
const process = require('process');
const request = require('request');

// Arguments variable
const args = process.argv;

if (args[2] != null) {
  const id = '18';
  const wa = 'https://swapi-api.alx-tools.com/api/people/' + id + '/';
  let count = 0;
  request(args[2], function (err, response, body) {
    if (!err && response.statusCode === 200) {
      const info = JSON.parse(body);
      for (let i = 0; i < info.results.length; i++) {
        if (info.results[i].characters.includes(wa)) {
          count++;
        }
      }
      console.log(count);
    }
  });
}
