/* global $ */

$(document).ready(() => {
  // URL for the Star Wars character API
  const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  // Select the <div> with id character using JQuery
  const characterDiv = $('#character');

  // Fetch data from the API
  $.get(apiUrl, (data) => {
    // Extract the character name from the response
    const characterName = data.name;

    // Update the text content of the <div> with the character name
    characterDiv.text(characterName);
  });
});
