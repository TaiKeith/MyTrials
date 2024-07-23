#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <movieID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);

    movieData.characters.forEach((characterUrl) => {
      request.get(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
	  console.error(charError);
	} else {
	  const characterData = JSON.parse(charBody);
	  console.log(characterData.name);
	}
      });
    });
  }
});
