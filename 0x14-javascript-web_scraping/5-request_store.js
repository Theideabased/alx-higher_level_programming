#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Request URL
const url = process.argv[2];
const filepath = process.argv[3];

request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) console.log(error);

  // print inside the filepath
  fs.writeFile(filepath, body, err => {
    if (err) {
      console.error(err);
    }
  });
});
