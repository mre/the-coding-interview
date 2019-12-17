#!/usr/bin/env node

let data = process.argv[2].split(',').map(Number);

for (let ip = 0; data[ip] !== 99; ip += 4) {
    switch (data[ip]) {
        case 1:
            data[data[ip + 3]] = data[data[ip + 1]] + data[data[ip + 2]];
            break;

        case 2:
            data[data[ip + 3]] = data[data[ip + 1]] * data[data[ip + 2]];
            break;

        default:
            throw new Error('Unknown opcode ' + data[ip]);
    }
}

console.log(data.join(','));
