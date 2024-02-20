#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);

    // Fetch characters details in order
    const charactersPromises = movieData.characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            const characterData = JSON.parse(charBody);
            resolve(characterData.name);
          }
        });
      });
    });

    // Resolve all promises and print character names
    Promise.all(charactersPromises)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(err => console.error(err));
  }
});
