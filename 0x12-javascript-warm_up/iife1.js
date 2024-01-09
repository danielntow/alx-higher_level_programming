(function () {
  let message = 'Hello, IIFE!';
  console.log(message);
})();
// Output: 'Hello, IIFE!'

const myModule = (function () {
  let privateVar = 'I am private';

  function privateFunction () {
    console.log('I am a private function');
  }

  return {
    publicVar: 'I am public',
    publicFunction: function () {
      console.log('I am a public function');
    }
  };
})();

console.log(myModule.publicVar); // Output: 'I am public'
myModule.publicFunction(); // Output: 'I am a public function'

(function (name) {
  console.log('Hello, ' + name);
})('Alice');
// Output: 'Hello, Alice'

const result = (function (a, b) {
  return a + b;
})(3, 4);
console.log(result); // Output: 7
