/* global $ */

$(document).ready(() => {
  // Select the input elements using JQuery
  const languageCodeInput = $('#language_code');
  const translateButton = $('#btn_translate');
  const helloDiv = $('#hello');

  // Attach a click event handler to the Translate button
  translateButton.click(() => {
    // Fetch the language code from the input
    const languageCode = languageCodeInput.val();

    // Fetch the translation from the API using JQuery AJAX
    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      success: (data) => {
        // Update the text content of the <div> with the translation
        helloDiv.text(data.hello);
      },
      error: () => {
        // Handle errors (e.g., invalid language code)
        helloDiv.text('Error: Invalid language code');
      }
    });
  });
});
