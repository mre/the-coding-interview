#!/usr/bin/env php
<?php

$chars = str_split($argv[1]);
natsort($chars);
$lower = $upper = $even = $odd = "";
foreach ($chars as $c) {
    if ('a' <= $c && $c <= 'z') {
        $lower .= $c;
    } elseif ('A' <= $c && $c <= 'Z') {
        $upper .= $c;
    } elseif (strpos("02468", $c) !== false) {
        $even .= $c;
    } else {
        $odd .= $c;
    }
}
echo "$lower$upper$even$odd";
