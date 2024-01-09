#!/usr/bin/node

function fetchData (url, callback) {
  // Simulated asynchronous operation fetching data
  setTimeout(function () {
    let data = 'Fetched data from ' + url;
    callback(data);
  }, 1000);
}

fetchData('example.com/api', function (result) {
  console.log(result); // Output after 1 second: 'Fetched data from example.com/api'
});

(function () {
  let secret = 'IIFE Secret';

  function getSecret () {
    return secret;
  }

  console.log(getSecret()); // Output: 'IIFE Secret'
})();
