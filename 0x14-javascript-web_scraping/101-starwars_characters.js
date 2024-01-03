#!/usr/bin/node

// For handling arguments and request
const process = require('process');
const request = require('request');

// Arguments variable
const args = process.argv;
const hit = {};

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

counterstop = 0;
counterx = 0;

function counter () {
  counterx++;
  if (counterx === counterstop) {
    for (const [key, value] of Object.entries(hit)) {
      console.log(value);
    }
  }
}

// Argument provided
if (args[2] != null) {
  const url = 'https://swapi-api.alx-tools.com/api/films/';
  const r = request(url + args[2], function (err, response, body) {
    if (!err && response.statusCode === 200) {
      allInfo(JSON.parse(body));
      counterstop = JSON.parse(body).characters.length;
    }
  });
}
