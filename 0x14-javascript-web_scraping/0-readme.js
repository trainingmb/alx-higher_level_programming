#!/usr/bin/node

//For handling arguments and files
const process = require('process');
const fs = require('fs');


//Arguments variable
const args = process.argv;

//Argument provided
if (args[2] != null){
	fs.readFile(args[2], {encoding: 'utf-8'}, function(err, data) => {
		if (err) {
			console.error(err);
			return;
		}
		console.log(data);
	});
}
