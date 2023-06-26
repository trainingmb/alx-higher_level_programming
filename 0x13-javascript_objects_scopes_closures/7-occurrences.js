#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(myFunction);

  function myFunction (value, index, array) {
    if (value === searchElement) {
	    count += 1;
    }
  }
  return count;
};
