#!/usr/bin/env node

let sum = 0;
process.argv[2].split('\n').forEach(x => {
    while (x > 0) {
        x = Math.max(0, Math.floor(x / 3) - 2);
        sum += x;
    }
});
console.log(sum);
