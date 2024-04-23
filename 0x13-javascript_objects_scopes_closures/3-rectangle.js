#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
    this.print = function () {
      let i, j;
      for (i = 0; i < h; i++) {
        for (j = 0; j < w; j++) {
	  console.log('X');
	}
      }
  }
};
