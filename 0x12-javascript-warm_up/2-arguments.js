#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log('No argument');
}
else if (process.argv.length === 3) {
  console.log('Argument found');
}
else (process.argv.length <= 4) {
  console.log('Arguments found');
}
