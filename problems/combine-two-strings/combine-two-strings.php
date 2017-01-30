<?php

declare(strict_types=1);

function is_shuffle(string $string1, string $string2, string $string3) : bool {
    if (strlen($string1) + strlen($string2) !== strlen($string3)) {
        return false;
    }

    $ptr1 = 0;
    $ptr2 = 0;
    foreach (str_split($string3) as $c) {
        if ($ptr1 < strlen($string1) && $c === $string1[$ptr1]) {
            $ptr1++;
            continue;
        } else if ($ptr2 < strlen($string2) && $c == $string2[$ptr2]) {
            $ptr2++;
            continue;
        } else {
            return false;
        }
    }
    return true;
}

assert(is_shuffle('abc', 'def', 'dabecf') === true);
assert(is_shuffle('bac', 'def', 'dabecf') === false);
assert(is_shuffle('otto', 'anna', '') === false);
assert(is_shuffle('otto', 'anna', 'oatntnoa') === true);
