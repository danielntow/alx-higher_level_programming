/* global $ */

$(document).ready(() => {
  // Add item to the list when the user clicks on DIV#add_item
  $('#add_item').click(() => {
    // Select the <ul> with class my_list using JQuery
    const myList = $('ul.my_list');

    // Create a new <li> element with text "Item"
    const newListItem = $('<li>').text('Item');

    // Append the new <li> element to the <ul>
    myList.append(newListItem);
  });

  // Remove the last item from the list when the user clicks on DIV#remove_item
  $('#remove_item').click(() => {
    // Select the last <li> element in the <ul> using JQuery
    const lastListItem = $('ul.my_list li:last-child');

    // Remove the last <li> element from the <ul>
    lastListItem.remove();
  });

  // Clear all items from the list when the user clicks on DIV#clear_list
  $('#clear_list').click(() => {
    // Select the <ul> with class my_list using JQuery
    const myList = $('ul.my_list');

    // Remove all <li> elements from the <ul>
    myList.empty();
  });
});
