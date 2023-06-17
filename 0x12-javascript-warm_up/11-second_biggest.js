#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let max1 = Number(process.argv[2]);
  let max2 = Number(process.argv[2]);

  for (let i = 0; i < process.argv.length; i++) {
    if (max1 < Number(process.argv[i])) {
      max1 = Number(process.argv[i]);
     }
   }

   for (let j = 0; j < process.argv.length; j++) {
      if (max2 < Number(process.argv[j]) && Number(process.argv[j]) !== max1) {
	max2 = Number(process.argv[j]);
       }
    }
    
    console.log(max2);
}  	 
