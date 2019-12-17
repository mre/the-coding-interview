#!/usr/bin/env node

class Pair {
    constructor(first, second) {
        this.first = first;
        this.second = second;
    }

    toString() {
        return '(' + this.first + ', ' + this.second + ')';
    }
}

const input = process.argv[2].split(',').map(Number);
const k = input.shift();
const seen = new Set();
const pairs = [];

input.forEach((n) => {
    const x = k - n;
    if (x !== n) {
        if (seen.has(x)) {
            pairs.push(new Pair(Math.min(x, n), Math.max(x, n)));
        } else {
            seen.add(n);
        }
    }
});

process.stdout.write('[');
pairs.forEach((pair, i) => {
    if (i !== 0) {
        process.stdout.write(', ');
    }
    process.stdout.write(pair.toString());
});
process.stdout.write(']');
