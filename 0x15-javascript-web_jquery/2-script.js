/* global $ */

$(document).ready(() => {
  // Select the <div> with id red_header using JQuery
  const redHeaderDiv = $('#red_header');

  // Attach a click event handler
  redHeaderDiv.click(() => {
    // Select the <header> element using JQuery
    const headerElement = $('header');

    // Update the text color to red
    headerElement.css('color', '#FF0000');
  });
});
