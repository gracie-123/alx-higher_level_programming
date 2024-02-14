#!/usr/bin/node

function getfactorial (n) {
  if (n === 1) {
    return 1;
  } else if (isNaN(n)) {
    return 1;
  } else {
    const f = n * getfactorial(n - 1);
    return f;
  }
}
const factr = process.argv[2];
const j = getfactorial(factr);
console.log(j);
