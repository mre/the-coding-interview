#!/usr/bin/env php
<?php

declare(strict_types=1);

$input = explode("\n", $argv[1]);
$parent = $input[0];
$parent_len = strlen($parent);
$child = $input[1];
$child_len = strlen($child);

function sum(string $s): int
{
    $result = 0;
    $limit = strlen($s);
    for ($i = 0; $i < $limit; ++$i) {
        $result += ord($s[$i]);
    }
    return $result;
}

if ($parent_len === $child_len) {
    echo (int)(sum($parent) == sum($child));
} else {
    $child_sum = sum($child);
    $result = 0;
    $start = 0;

    do {
        if (sum(substr($parent, $start, $child_len)) === $child_sum) {
            ++$result;
        }
        ++$start;
    } while (($start + $child_len) < $parent_len);

    echo $result;
}
