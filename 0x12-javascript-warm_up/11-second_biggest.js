#!/usr/bin/node

if (process.argv.length <= 1) {
  console.log('0');
} else {
  let max1 = process.argv[0];
  let max2 = process.argv[0];

  for (let i = 0; i < process.argv.length; i++) {
    if (max1 < process.argv[i]) {
      max1 = process.argv[i];
     }
   }

   for (let j = 0; j < process.argv.length; j++) {
      if (max2 < process.argv[j] && process.argv[j] !== max1) {
	max2 = process.argv[j];
       }
    }
    
    console.log(max2);
}  	 
