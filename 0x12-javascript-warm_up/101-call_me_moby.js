#!/usr/bin/node

// The externul function called moby
exports.callMeMoby = function (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
};
