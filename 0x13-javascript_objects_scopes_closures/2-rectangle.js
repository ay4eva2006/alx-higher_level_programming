#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
<<<<<<< HEAD
    if ((w > 0) && (h > 0)) {
=======
    if (w <= 0 || h <= 0) {
      return {};
    } else {
>>>>>>> 9888f9660c2c76acfdb0f4e0737c568a64e3feac
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
