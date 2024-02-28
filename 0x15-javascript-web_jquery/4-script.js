/* global $ */

$(document).ready(() => {
  // Select the <div> with id toggle_header using JQuery
  const toggleHeaderDiv = $('#toggle_header');

  // Attach a click event handler
  toggleHeaderDiv.click(() => {
    // Select the <header> element using JQuery
    const headerElement = $('header');

    // Toggle between red and green classes
    headerElement.toggleClass('red green');
  });
});
