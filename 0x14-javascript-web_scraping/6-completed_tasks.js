#!/usr/bin/node

// For handling arguments and request
const process = require('process');
const request = require('request');

// Arguments variable
const args = process.argv;

// Argument provided
if (args[2] != null) {
  const res = {};
  request(args[2], function (err, response, body) {
    if (!err && response.statusCode === 200) {
      const info = JSON.parse(body);
      for (let i = 0; i < info.length; i++) {
        if (info[i].completed) {
          if (res[info[i].userId] === undefined) {
            res[info[i].userId] = 1;
          } else {
            res[info[i].userId]++;
	  }
        }
      }
      console.log(res);
    }
  });
}
