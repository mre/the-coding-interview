#!/usr/bin/env node

if (process.argv.length !== 3) {
    throw new Error('Missing required input.');
}

function apply(data, i, op) {
    data[data[i + 3]] = op(data[data[i + 1]], data[data[i + 2]]);
}

let data = process.argv[2].split(',').map(Number);

for (let i = 0; data[i] !== 99; i += 4) {
    switch (data[i]) {
        case 1:
            apply(data, i, (lhs, rhs) => lhs + rhs);
            break;

        case 2:
            apply(data, i, (lhs, rhs) => lhs * rhs);
            break;

        default:
            throw new Error('Unknown opcode ' + data[i] + ': something went wrong.');
    }
}

console.log(data.join(','));
