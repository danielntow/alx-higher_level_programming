/* global $ */

$(document).ready(function () {
  // Select the <div> with id red_header using JQuery
  const redHeaderDiv = $('#red_header');

  // Attach a click event handler
  redHeaderDiv.click(function () {
    // Select the <header> element using JQuery
    const headerElement = $('header');

    // Add the class 'red' to the <header> element
    headerElement.addClass('red');
  });
});
