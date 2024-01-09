function createHeavyObject () {
  let bigData = new Array(10000).fill('x'); // Simulating a large amount of data

  return function () {
    console.log(bigData.length);
  };
}

let closure = createHeavyObject();
closure(); // Output: 10000

// The closure retains a reference to bigData, preventing it from being garbage collected

function fetchData (url, callback) {
  let data = null; // Explicitly setting data to null

  setTimeout(function () {
    data = 'Fetched data from ' + url;
    callback(data);
    data = null; // Release data after usage
  }, 1000);
}
