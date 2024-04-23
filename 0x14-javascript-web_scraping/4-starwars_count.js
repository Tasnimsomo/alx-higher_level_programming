#!/usr/bin/node

const request = require('request');
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;
const url = baseUrl + characterId;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const movie = JSON.parse(body);
  console.log(movie.films.length);
});
