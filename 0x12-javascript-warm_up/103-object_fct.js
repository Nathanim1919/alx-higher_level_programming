#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

myObject.incr = function() {
  myObject.value += 1;
}
