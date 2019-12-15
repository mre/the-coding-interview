#!/usr/bin/env php
<?php

declare(strict_types=1);

$data = array_map(fn($it) => (int)$it, explode(',', $argv[1]));

for ($ip = 0; $data[$ip] !== 99; $ip += 4) {
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

echo implode(',', $data);
