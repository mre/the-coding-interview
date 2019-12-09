#!/usr/bin/env node

if (process.argv.length !== 3) {
    throw new Error('Missing required input.');
}

function apply(data, i, op) {
    data[data[i + 3]] = op(data[data[i + 1]], data[data[i + 2]]);
}

function intComputer(data) {
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
    return data[0];
}

let input = process.argv[2].split(',').map(Number);

for (let noun = 0; noun < 100; ++noun) {
    for (let verb = 0; verb < 100; ++verb) {
        let data = input.slice();
        data[1] = noun;
        data[2] = verb;
        if (intComputer(data) === 19690720) {
            console.log(100 * noun + verb);
            process.exit(0);
        }
    }
}
process.exit(1);
