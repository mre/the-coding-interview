<?php
// NOT multi-byte safe!

function char_sum(string $string): int {
    $sum = 0;
    for ($i = 0, $l = strlen($string); $i < $l; ++$i) $sum += ord($string{$i});
    return $sum;
}

function can_scramble(string $input, string $output): bool {
    return strlen($input) === strlen($output) && char_sum($input) === char_sum($output);
}

assert(can_scramble("abc", "abc") === true);
assert(can_scramble("abc", "cba") === true);
assert(can_scramble("a", "aaaaaaaaaa") === false); // Word length does not match
assert(can_scramble("abc", "cbad") === false);     // Word length does not match
assert(can_scramble("aab", "bba") === false);      // word length matches, character count not
