#!/usr/bin/env node

console.log(process.argv[2].split('\n').reduce((acc, x) => acc + Math.floor(x / 3) - 2, 0));
