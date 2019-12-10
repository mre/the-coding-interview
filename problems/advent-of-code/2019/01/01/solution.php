#!/usr/bin/env php
<?php

$sum = 0;
foreach (explode("\n", $argv[1]) as $i => $n) {
    $sum += floor($n / 3) - 2;
}
echo "$sum\n";
