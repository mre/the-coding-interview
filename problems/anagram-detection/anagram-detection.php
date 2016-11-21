<?php

function hashString($str)
{
  $hashMap = [
    'a' => 2,
    'b' => 3,
    'c' => 5,
    'd' => 7,
    'e' => 11,
    'f' => 13,
    'g' => 17,
    'h' => 19,
    'i' => 23,
    'j' => 29,
    'k' => 31,
    'l' => 37,
    'm' => 41,
    'n' => 43,
    'o' => 47,
    'p' => 53,
    'q' => 59,
    'r' => 61,
    's' => 67,
    't' => 71,
    'u' => 73,
    'v' => 79,
    'w' => 83,
    'x' => 89,
    'y' => 97,
    'z' => 101,
    'A' => 103,
    'B' => 107,
    'C' => 109,
    'D' => 113,
    'E' => 127,
    'F' => 131,
    'G' => 137,
    'H' => 139,
    'I' => 149,
    'J' => 151,
    'K' => 163,
    'L' => 167,
    'M' => 173,
    'N' => 179,
    'O' => 181,
    'P' => 191,
    'Q' => 193,
    'R' => 197,
    'S' => 199,
    'T' => 211,
    'U' => 223,
    'V' => 227,
    'W' => 229,
    'X' => 233,
    'Y' => 239,
    'Z' => 241
  ];

  $hash = 1;
  foreach (str_split($str) as $char)
  {
    $hash *= $hashMap[$char];
  }
  return $hash;
}

function anagramDetection($parent, $child)
{
  $len = strlen($child);
  $childHash = hashString($child);
  $matches = [];

  for ($start = 0; $start < strlen($parent) - $len; $start++)
  {
    $parentSubstr = substr($parent, $start, $len);
    $parentHash = hashString($parentSubstr);
    if ($parentHash === $childHash)
    {
      $matches[] = $parentSubstr;
    }
  }
  return $matches;
}

print_r(anagramDetection('AdnBndAndBdaBn', 'dAn')); // 4 ("Adn", "ndA", "dAn", "And")
