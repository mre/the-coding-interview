<?php

function substrings($string)
{
  $result = [];
  for ($start = 0; $start < strlen($string); $start++)
  {
    for ($length = 1; $length <= strlen($string) - $start; $length++)
    {
      $result[] = substr($string, $start, $length);
    }
  }
  return $result;
}

print_r(substrings("abc")); // => ["a", "b", "c", "ab", "bc", "abc"]
