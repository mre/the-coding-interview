<?php
function sorted_chars(string $input): array {
    $chars = str_split($input);
    sort($chars);
    return $chars;
}
function can_scramble(string $input, string $output): bool {
    return strlen($input) === strlen($output) && sorted_chars($input) === sorted_chars($output);
}
assert(can_scramble("abc", "abc") === true);
assert(can_scramble("abc", "cba") === true);
assert(can_scramble("a", "aaaaaaaaaa") === false); // Word length does not match
assert(can_scramble("abc", "cbad") === false);     // Word length does not match
assert(can_scramble("aab", "bba") === false);      // Word length matches, character count not
assert(can_scramble("ac", "bb") === false);        // Word length matches, wrong characters
