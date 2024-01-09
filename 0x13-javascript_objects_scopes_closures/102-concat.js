#!/usr/bin/node

const fs = require('fs');

const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

const concatFiles = (file1, file2, destination) => {
  try {
    const data1 = fs.readFileSync(file1, 'utf8');
    const data2 = fs.readFileSync(file2, 'utf8');
    const concatenatedData = data1 + data2;
    fs.writeFileSync(destination, concatenatedData);
    console.log(`Files ${file1} and ${file2} concatenated to ${destination}`);
  } catch (err) {
    console.error(err);
  }
};

concatFiles(sourceFile1, sourceFile2, destinationFile);
