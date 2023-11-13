#!/usr/bin/node

const size = process.argv[2];
const num = parseInt(size);
const character = 'X';

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log(character.repeat(num));
  }
}
