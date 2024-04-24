#!/usr/bin/node

exports.esrever = function (list) {
  const Rlist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    Rlist.push(list[i]);
  }
  return Rlist;
};
