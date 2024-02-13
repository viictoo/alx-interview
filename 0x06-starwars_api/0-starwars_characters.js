#!/usr/bin/node
/* a script that prints all characters of a Star Wars movie:
*/
// const request = require('request');
// const util = require('util');
const request = require('request');
// const request = util.promisify(require('request'));
const id = process.argv[2];
const apiURL = 'https://swapi-api.hbtn.io/api/films/';

// Serial Execution Version
function getXters (urls, idx) {
  request(urls[idx], (err, res, body) => {
    if (err) return console.error(err);
    console.log(JSON.parse(body).name);
    if (idx < urls.length - 1) {
      getXters(urls, idx + 1);
    }
  });
}

// Parallel Exectution Version
function fetchXters (urls) {
  // Create an array of promises from the request calls
  const fetchPromises = urls.map((url) => request({ url }));

  Promise.all(fetchPromises)
    .then((responses) => {
      responses.forEach((resp) => console.log(JSON.parse(resp.body).name));
    })
    .catch((err) => {
      console.error(err);
    });
}

request(apiURL + id, (err, res, body) => {
  if (err) return console.error(err);
  const allCharacters = JSON.parse(body).characters;
  getXters(allCharacters, 0);
  if (!allCharacters) {
    fetchXters(allCharacters);
  }
});
