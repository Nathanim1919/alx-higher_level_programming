#!/usr/bin/node

const list = require('./100-data.js');

const newList = [];

list.map((item, index) => newList.push(item * index));
console.log(list);
console.log(newList);
