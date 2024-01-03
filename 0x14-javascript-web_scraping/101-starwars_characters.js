#!/usr/bin/node

// For handling arguments and request
const process = require('process');
const request = require('request');

// Variables
const args = process.argv;
const hit = {};
var counterstop = 0;
var counterx = 0;

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
      const j = JSON.parse(body);
      hit[j.url.split('/')[5]] = j.name;
      counter();
    }
  });
}

//Counter for when to log
function counter () {
  counterx++;
  if (counterx === counterstop) {
    for (const [key, value] of Object.entries(hit)) {
      console.log(value);
      if (key === '1') {
        counterx++;
      }
    }
  }
}

// Argument provided
if (args[2] != null) {
  const url = 'https://swapi-api.alx-tools.com/api/films/';
  request(url + args[2], function (err, response, body) {
    if (!err && response.statusCode === 200) {
      allInfo(JSON.parse(body));
      counterstop = JSON.parse(body).characters.length;
    }
  });
}
