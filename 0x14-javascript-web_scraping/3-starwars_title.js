#!/usr/bin/node

const request = require('request');
const Id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${Id}`;

request(url, (error, res, body) => {
  if (error) {
    return console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
