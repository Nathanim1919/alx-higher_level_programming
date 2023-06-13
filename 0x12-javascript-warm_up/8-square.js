#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    for (let j = 0; j < Number(process.argv[2]; j++)) {
      console.log("x");
    }
    console.log('\n');
  }
}
