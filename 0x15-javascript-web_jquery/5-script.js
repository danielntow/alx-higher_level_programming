/* global $ */

$(document).ready(() => {
  // Select the <div> with id add_item using JQuery
  const addItemDiv = $('#add_item');

  // Attach a click event handler
  addItemDiv.click(() => {
    // Select the <ul> with class my_list using JQuery
    const myList = $('ul.my_list');

    // Create a new <li> element with text "Item"
    const newListItem = $('<li>').text('Item');

    // Append the new <li> element to the <ul>
    myList.append(newListItem);
  });
});
