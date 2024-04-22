#!/usr/bin/node

let i, j, x, row = "";
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  x = Number(process.argv[2]);
}

for (i = 0; i < x; i++) {
  row = "";
  for (j = 0; j < x; j++) {
    row += "X";
  }
  console.log(row);
}
