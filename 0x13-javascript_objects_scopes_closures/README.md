# 0x13. JavaScript - Objects, Scopes and Closures

![Static Badge](https://img.shields.io/badge/JavaScript-black?logo=JavaScript&logoColor=%23f7df1e)  ![Static Badge](https://img.shields.io/badge/AbdullahHR10-%230359AE?logo=Github&logoColor=%23000000)


# Files

## 0-rectangle.js
Empty class Rectangle that defines a rectangle
## 1-rectangle.js
Class Rectangle that defines a rectangle:<br>
The constructor takes 2 arguments w and h<br>
Instance attribute width with the value of w<br>
Instance attribute height with the value of h<br>
## 2-rectangle.js
Class Rectangle that defines a rectangle<br>
Instance attribute width with the value of w<br>
Instance attribute height with the value of h<br>
If w or h is equal to 0 or not a positive integer, It creates an empty object<br>
## 3-rectangle.js
Class Rectangle that defines a rectangle<br>
Instance attribute width with the value of w<br>
Instance attribute height with the value of h<br>
If w or h is equal to 0 or not a positive integer, It creates an empty object<br>
Instance method called print() that prints the rectangle using the character X<br>
## 4-rectangle.js
Class Rectangle that defines a rectangle<br>
Instance attribute width with the value of w<br>
Instance attribute height with the value of h<br>
If w or h is equal to 0 or not a positive integer, It creates an empty object<br>
Instance method called print() that prints the rectangle using the character X<br>
Instance method called rotate() that exchanges the width and the height of the rectangle<br>
Instance method called double() that multiples the width and the height of the rectangle by 2<br>
## 5-square.js
Class Square that defines a square and inherits from Rectangle of 4-rectangle.js<br>
The constructor takes 1 argument: size<br>
The constructor of Rectangle is called by using super()<br>
## 6-square.js
Class Square that defines a square and inherits from Square of 5-square.js<br>
Instance method called charPrint(c) that prints the rectangle using the character c<br>
If c is undefined, It uses the character X<br>
## 7-occurrences.js
Returns the number of occurrences in a list<br>
Prototype: exports.nbOccurences = function (list, searchElement)<br>
## 8-esrever.js
Function that returns the reversed version of a list<br>
Prototype: exports.esrever = function (list)<br>
## 9-logme.js
Function that prints the number of arguments already printed and the new argument value<br>
Prototype: exports.logMe = function (item)<br>
Output format: <number arguments already printed>: <current argument value><br>
## 10-converter.js
Function that converts a number from base 10 to another base passed as argument<br>
Prototype: exports.converter = function (base)<br>
## 100-map.js
Script that imports an array and computes a new array<br>
Imports list from the file 100-data.js<br>
Creates a new list with each value equal to the value of the initial list, multipled by the index in the list<br>
Prints both the initial list and the new list<br>
## 100-data.js
Contains a list<br>
## 101-sorted.js
Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence<br>
Imports dict from the file 101-data.js<br>
In the new dictionary:<br>
A key is a number of occurrences<br>
A value is the list of user ids<br>
Prints the new dictionary at the end<br>
## 101-data.js
Contains a dictionary<br>
## 102-concat.js
Script that concats 2 files<br>
The first argument is the file path of the first source file<br>
The second argument is the file path of the second source file<br>
The third argument is the file path of the destination
