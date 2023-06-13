#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

myObject.incr = function() {
  this.alue += 1;
}
