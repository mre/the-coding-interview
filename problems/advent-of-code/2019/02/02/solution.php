#!/usr/bin/env php
<?php

declare(strict_types=1);

function int_computer(array $data): int {
    for ($ip = 0; $data[$ip] != 99; $ip += 4) {
        switch ($data[$ip]) {
            case 1:
                $data[$data[$ip + 3]] = $data[$data[$ip + 1]] + $data[$data[$ip + 2]];
                break;

            case 2:
                $data[$data[$ip + 3]] = $data[$data[$ip + 1]] * $data[$data[$ip + 2]];
                break;

            default:
                throw new Error("Unknown opcode {$data[$ip]}");
        }
    }

    return $data[0];
}

$input = array_map(fn($it) => (int)$it, explode(',', $argv[1]));

for ($noun = 0; $noun < 100; ++$noun) {
    for ($verb = 0; $verb < 100; ++$verb) {
        $data = $input;
        $data[1] = $noun;
        $data[2] = $verb;
        if (int_computer($data) === 19690720) {
            echo 100 * $noun + $verb;
            exit(0);
        }
    }
}
exit(1);
