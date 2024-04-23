#!/usr/bin/node

const request = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;

request.get(baseUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body);
  let counter = 0;
  for (const film of films.results) {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      counter++;
    }
  }

  console.log(counter);
});
