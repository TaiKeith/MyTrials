#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./script.js <URL> <file path>');
  process.exit(1);
}

const url = process.argv[2];
const file = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(file, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      }
    });
  }
});
