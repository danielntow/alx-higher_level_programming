/* global $ */

$(document).ready(() => {
  // URL for the Star Wars movies API
  const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Select the <ul> with id list_movies using JQuery
  const listMoviesUl = $('#list_movies');

  // Fetch data from the API
  $.get(apiUrl, (data) => {
    // Iterate through each movie and append its title to the list
    data.results.forEach((movie) => {
      // Create a new <li> element with the movie title
      const listItem = $('<li>').text(movie.title);

      // Append the <li> element to the <ul>
      listMoviesUl.append(listItem);
    });
  });
});
