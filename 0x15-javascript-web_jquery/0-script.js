// 0-script.js

const changeHeaderColor = () => {
  // Select the header element using document.querySelector
  const headerElement = document.querySelector('header');

  // Update the text color to red (#FF0000)
  headerElement.style.color = '#FF0000';
};

document.addEventListener('DOMContentLoaded', changeHeaderColor);
