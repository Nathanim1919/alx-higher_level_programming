#!/usr/bin/node

exports.addMemaybe = function (number, theFunction) {
  theFunction(++number);
};
