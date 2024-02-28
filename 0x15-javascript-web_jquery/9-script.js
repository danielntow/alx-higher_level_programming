/* global $ */

$(document).ready(() => {
    // URL for fetching the translation of "hello"
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

    // Select the <div> with id hello using JQuery
    const helloDiv = $('#hello');

    // Fetch data from the API
    $.get(apiUrl, (data) => {
        // Update the text content of the <div> with the translation
        helloDiv.text(data.hello);
    });
});
