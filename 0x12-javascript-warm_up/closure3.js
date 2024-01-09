const CounterModule = (function () {
  let count = 0;

  function increment () {
    count++;
    console.log(count);
  }

  function reset () {
    count = 0;
    console.log('Counter reset');
  }

  return {
    increment: increment,
    reset: reset
  };
})();

CounterModule.increment(); // Output: 1
CounterModule.increment(); // Output: 2
CounterModule.reset(); // Output: 'Counter reset'

function createButton () {
  let clickCount = 0;

  const button = document.createElement('button');
  button.textContent = 'Click me';

  button.addEventListener('click', function () {
    clickCount++;
    console.log(`Button clicked ${clickCount} times`);
  });

  document.body.appendChild(button);
}

// createButton()

function add (x) {
  return function (y) {
    return x + y;
  };
}

const addFive = add(5);
console.log(addFive(3)); // Output: 8
