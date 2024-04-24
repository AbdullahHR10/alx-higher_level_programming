# 0x13. JavaScript - Objects, Scopes and Closures

![Static Badge](https://img.shields.io/badge/JavaScript-black?logo=JavaScript&logoColor=%23f7df1e)  ![Static Badge](https://img.shields.io/badge/AbdullahHR10-%230359AE?logo=Github&logoColor=%23000000)


# Files

## 0-rectangle.js
Empty class Rectangle that defines a rectangle
## 1-rectangle.js
Class Rectangle that defines a rectangle:
The constructor takes 2 arguments w and h
Instance attribute width with the value of w
Instance attribute height with the value of h
## 2-rectangle.js
Class Rectangle that defines a rectangle
Instance attribute width with the value of w
Instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, It creates an empty object
## 3-rectangle.js
Class Rectangle that defines a rectangle
Instance attribute width with the value of w
Instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, It creates an empty object
Instance method called print() that prints the rectangle using the character X
## 4-rectangle.js
Class Rectangle that defines a rectangle
Instance attribute width with the value of w
Instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, It creates an empty object
Instance method called print() that prints the rectangle using the character X
Instance method called rotate() that exchanges the width and the height of the rectangle
Instance method called double() that multiples the width and the height of the rectangle by 2
## 5-square.js
Class Square that defines a square and inherits from Rectangle of 4-rectangle.js
The constructor takes 1 argument: size
The constructor of Rectangle is called by using super()
## 6-square.js
Class Square that defines a square and inherits from Square of 5-square.js
Instance method called charPrint(c) that prints the rectangle using the character c
If c is undefined, It uses the character X
## 7-occurrences.js
Returns the number of occurrences in a list
Prototype: exports.nbOccurences = function (list, searchElement)
## 8-esrever.js
Function that returns the reversed version of a list
Prototype: exports.esrever = function (list)
## 9-logme.js
Function that prints the number of arguments already printed and the new argument value
Prototype: exports.logMe = function (item)
Output format: <number arguments already printed>: <current argument value>
## 10-converter.js
Function that converts a number from base 10 to another base passed as argument
Prototype: exports.converter = function (base)
## 100-map.js
Script that imports an array and computes a new array
Imports list from the file 100-data.js
Creates a new list with each value equal to the value of the initial list, multipled by the index in the list
Prints both the initial list and the new list
## 100-data.js
Contains a list
## 101-sorted.js
Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence
Imports dict from the file 101-data.js
In the new dictionary:
A key is a number of occurrences
A value is the list of user ids
Prints the new dictionary at the end
## 101-data.js
Contains a dictionary
## 102-concat.js
Script that concats 2 files
The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination
