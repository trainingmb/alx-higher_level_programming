#!/usr/bin/node

exports.esrever = function (list){
    let x = list.length - 1;
    let reved = [];
    while (x >= 0) {
        reved.push(list[x]);
        x -= 1;
    }
    return reved; 
};
