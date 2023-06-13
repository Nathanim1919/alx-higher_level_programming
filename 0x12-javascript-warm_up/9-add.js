#!/usr/bin/node
function add(a, b) {
  if (isNaN(a) || isNaN(b) || process.argv.length !== 2) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}
