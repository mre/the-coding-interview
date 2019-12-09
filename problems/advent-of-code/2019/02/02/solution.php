#!/usr/bin/env php
<?php

declare(strict_types=1);

if ($argc != 2) {
    throw new InvalidArgumentException("Missing required input.");
}

function apply(array &$data, int $i, callable $op): void
{
    $data[$data[$i + 3]] = $op($data[$data[$i + 1]], $data[$data[$i + 2]]);
}

function int_computer(array $data): int
{
    for ($i = 0; $data[$i] != 99; $i += 4) {
        switch ($data[$i]) {
            case 1:
                apply($data, $i, fn($lhs, $rhs) => $lhs + $rhs);
                break;

            case 2:
                apply($data, $i, fn($lhs, $rhs) => $lhs * $rhs);
                break;

            default:
                throw new AssertionError("Unknown opcode {$data[$i]}: something went wrong");
        }
    }
    return $data[0];
}

$input = array_map(fn($e) => (int)$e, explode(',', $argv[1]));

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
