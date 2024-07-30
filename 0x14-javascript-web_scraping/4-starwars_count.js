#!/usr/bin/node
const request = require('request');
const characterId = 18;
const url = process.argv[2];
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  const films = data.results;
  const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;
  const count = films.filter(film => film.characters.includes(characterUrl)).length;
  console.log(count);
});
