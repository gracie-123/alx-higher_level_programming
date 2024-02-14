#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const fs = require('fs');
const path = require('path');

const pathFile1 = path.resolve(path.dirname(__filename), './' + argv[2]);
const pathFile2 = path.resolve(path.dirname(__filename), './' + argv[3]);
const pathFile3 = path.resolve(path.dirname(__filename), './' + argv[4]);

const input = fs.readFileSync(pathFile1, 'utf8') + fs.readFileSync(pathFile2, 'utf8');
fs.writeFileSync(pathFile3, input);
