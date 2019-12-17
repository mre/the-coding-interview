#!/usr/bin/env php
<?php

final class Pair {
    public int $first;
    public int $second;

    public function __construct(int $first, int $second) {
        $this->first = $first;
        $this->second = $second;
    }

    public function __toString() {
        return "({$this->first}, {$this->second})";
    }
}

$input = json_decode("[{$argv[1]}]", false);
$k = array_shift($input);
$pairs = [];
$seen = [];
foreach ($input as $n) {
    $x = $k - $n;
    if ($x !== $n) {
        if (isset($seen[$x])) {
            $pairs[] = new Pair(min($x, $n), max($x, $n));
        } else {
            $seen[$n] = true;
        }
    }
}

echo '[';
foreach ($pairs as $i => $pair) {
    if ($i !== 0) {
        echo ', ';
    }
    echo $pair;
}
echo ']';
