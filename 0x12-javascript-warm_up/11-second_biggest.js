#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  const secondBiggest = args.sort((a, b) => b - a)[1];
  console.log(secondBiggest);
}
