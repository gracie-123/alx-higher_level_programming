#!/usr/bin/node

/* searches the second biggest integer in the list of arguments */
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
}
const myArgs = [];
if (args.length > 3) {
  for (let i = 0; args[i]; i++) {
    if (!(isNaN(args[i]))) {
      myArgs.push(args[i]);
    }
  }
  /* sort array to return items in ascending order */
  myArgs.sort(function (a, b) { return a - b; });
  /* slice the array to ge last two items, returning the second biggest */
  const secBig = myArgs.slice(-2, -1);
  console.log(secBig[0]);
}
