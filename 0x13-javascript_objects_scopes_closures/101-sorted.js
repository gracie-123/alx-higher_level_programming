#!/usr/bin/node
const importDict = require('./101-data');

const _dict = importDict.dict;
const newDict = {};

for (const userId in _dict) {
  const occurrences = _dict[userId];
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);
}
console.log(newDict);
