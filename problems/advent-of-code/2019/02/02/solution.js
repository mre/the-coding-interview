#!/usr/bin/env node

function intComputer(data) {
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
    return data[0];
}

const input = process.argv[2].split(',').map(Number);

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
