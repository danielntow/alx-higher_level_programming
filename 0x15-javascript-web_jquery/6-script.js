/* global $ */

$(document).ready(() => {
  // Select the <div> with id update_header using JQuery
  const updateHeaderDiv = $('#update_header');

  // Attach a click event handler
  updateHeaderDiv.click(() => {
    // Select the <header> element using JQuery
    const headerElement = $('header');

    // Update the text to "New Header!!!"
    headerElement.text('New Header!!!');
  });
});
