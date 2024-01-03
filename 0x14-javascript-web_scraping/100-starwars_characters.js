#!/usr/bin/node

// For handling arguments and request
const process = require('process');
const request = require('request');

// Arguments variable
const args = process.argv;

// Iterate through info
function allInfo (info) {
  for (let i = 0; i < info.characters.length; i++) {
    getPeople(info.characters[i]);
  }
}

// Get People
function getPeople (purl) {
  request(purl, function (err, response, body) {
    if (!err && response.statusCode === 200) {
      console.log(JSON.parse(body).name);
    }
  });
}

// Argument provided
if (args[2] != null) {
  const url = 'https://swapi-api.alx-tools.com/api/films/';
  request(url + args[2], function (err, response, body) {
    if (!err && response.statusCode === 200) {
      allInfo(JSON.parse(body));
    }
  });
}
