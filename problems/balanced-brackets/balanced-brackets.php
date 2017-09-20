<?php

function balanced(string $s) {
    $opposite = [
        '(' => ')',
        '[' => ']',
        '{' => '}',
    ];
    $charArray = str_split($s);
    $stack = new SplStack();
    foreach ($charArray as $c) {
        if ($c === '(' || $c === '[' || $c === '{') {
            $stack->push($c);
            continue;
        }
        if ($c === ')' || $c === ']' || $c === '}') {
            try {
                $last = $stack->pop();
                if ($opposite[$last] !== $c) {
                    return false;
                }
            } catch (\Exception $e) {
                return false;
            }
            continue;
        }
    }

    return $stack->isEmpty();
}


assert(balanced('()[]{}(([])){[()][]}'));
assert(!balanced('[(])'));
assert(balanced('()[][[{{}}]]'));
assert(!balanced(')[}[[{{}]]'));