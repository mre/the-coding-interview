#!/usr/bin/env php
<?php

$sum = 0;
foreach (explode("\n", $argv[1]) as $n) {
    while ($n > 0) {
        $n = max(0, floor($n / 3) - 2);
        $sum += $n;
    }
}
echo "$sum\n";
