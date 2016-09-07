<?php
  
/**
 * Runtime complexity: O(n)
 */
function canScramble($source, $dest)
{
  // Quick and fast sanity check
  if (strlen($dest) != strlen($source))
  {
    return false;
  }

  // The string lengths match.
  // Create associative array for character counts in source and dest

  $chars_source = [];
  foreach (str_split($source) as $char)
  {
    if (array_key_exists($char, $chars_source))
    {
      $chars_source[$char] += 1;
    }
    else
    {
      $chars_source[$char] = 1;
    }
  }
  $chars_dest = [];
  foreach (str_split($dest) as $char)
  {
    if (array_key_exists($char, $chars_dest))
    {
      $chars_dest[$char] += 1;
    }
    else
    {
      $chars_dest[$char] = 1;
    }
  }

  foreach ($chars_dest as $char => $count)
  {
    if (!array_key_exists($char, $chars_source) || $chars_source[$char] != $count)
    {
      return false;
    }
  }

  return true;
}

assert(canScramble("abc", "abc") === True);
assert(canScramble("abc", "cba") === True);
assert(canScramble("a", "aaaaaaaaaa") === False); // Word length does not match
assert(canScramble("abc", "cbad") === False);     // Word length does not match
assert(canScramble("aab", "bba") === False);      // word length matches, character count not
