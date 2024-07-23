#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <movieID>');
  process.exit(1);
}

const charId = process.argv[2];
const apiUrl = 'https://api.tvmaze.com/shows/${charId}';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
