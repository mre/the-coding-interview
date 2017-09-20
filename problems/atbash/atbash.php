<?php

function atbash(string $s) {
    $x = "";
    foreach (str_split(strtolower($s)) as $c) {
        $x .= chr(ord('z') - (ord($c) - ord('a')));
    }
    return $x;
}

assert(atbash('abcdefghijklmnopqrstuvwxyz') === 'zyxwvutsrqponmlkjihgfedcba');
assert(atbash('old') === 'low');
