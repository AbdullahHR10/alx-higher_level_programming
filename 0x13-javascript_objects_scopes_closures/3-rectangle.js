#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    this.print = function () {
      let i;
      const row = 'X'.repeat(w);
      for (i = 0; i < h; i++) {
        console.log(row);
      }
    };
  }
};
