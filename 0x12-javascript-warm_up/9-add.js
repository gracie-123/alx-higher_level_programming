#!/usr/bin/node
// this script print the addition of (2) integers
const args = process.argv.slice(2);
const firstInt = parseInt(args[0]);
const secondInt = parseInt(args[1]);

function add (a, b) {
  console.log(a + b);
}

add(firstInt, secondInt);
