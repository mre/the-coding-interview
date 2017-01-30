<?php

declare(strict_types=1);

function is_shuffle(string $string1, string $string2, string $string3) : bool {
    if ($string1 . $string2 . $string3 === '') {
        return false;
    }

    $string1Length = strlen($string1);
    if ($string1Length + strlen($string2) !== strlen($string3)) {
        return false;
    }

    $pattern = [];
    $replace = '';
    for ($i=0; $i<$string1Length; $i++) {
        $pattern[] = '(?:(?:' . preg_quote($string1[$i], '/') .')([^\\1]*))';
        $replace .= '$' . ($i + 1);
    }

    return preg_replace('/' . implode('', $pattern) . '/', $replace, $string3) === $string2;
}

assert(is_shuffle('abc', 'def', 'dabecf') === true);
assert(is_shuffle('bac', 'def', 'dabecf') === false);
assert(is_shuffle('otto', 'anna', '') === false);
assert(is_shuffle('otto', 'anna', 'oatntnoa') === true);
