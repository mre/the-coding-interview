<?php

function closedLoops($number)
{
  $loopMap = [
    '0' => 1,
    '1' => 0,
    '2' => 0,
    '3' => 0,
    '4' => 0,
    '5' => 0,
    '6' => 1,
    '7' => 0,
    '8' => 2,
    '9' => 1
  ];
  $loopCount = 0;
  foreach (str_split($number) as $i)
  {
    $loopCount += $loopMap[$i];
  }
  return $loopCount;
}

assert(closedLoops(2581) == 2);
assert(closedLoops(10000) == 4);
assert(closedLoops(16789) == 4);
