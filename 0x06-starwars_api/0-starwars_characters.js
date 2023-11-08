#!/usr/bin/node

const request = require('request');
const args = process.argv;
let filmID = 0;
if (args.length > 2) {
  filmID = Number(args[2]);
}

const url = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

function getName (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (!error) {
        const data = JSON.parse(body);
        resolve(data.name);
      } else {
        reject(error);
      }
    });
  });
}

request.get(url, async (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const characters = data.characters;
    for (const url of characters) {
      const name = await getName(url);
      console.log(name);
    }
  }
});
