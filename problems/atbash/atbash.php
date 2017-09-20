<?php

function atbash(string $s) {
    if (ord(strtolower($s)) < ord('a') || ord(strtolower($s)) > ord('z')) {
        return $s;
    }
    $x = '';
    foreach (str_split(strtolower($s)) as $c) {
        $x .= chr(ord('z') - (ord($c) - ord('a')));
    }
    return $x;
}

assert(atbash('abcdefghijklmnopqrstuvwxyz') === 'zyxwvutsrqponmlkjihgfedcba');
assert(atbash('old') === 'low');
assert(atbash('LOW') === 'old');
assert(atbash('') === '');
assert(atbash('?') === '?');
