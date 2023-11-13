#!/usr/bin/node

// The externul function called call me Maybe
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
