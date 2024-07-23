#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <API URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const moviesData = JSON.parse(body);
    const moviesWithAntilles = moviesData.results.filter((movie) =>
      movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
    console.log(`${moviesWithAntilles.length}`);
  }
});
