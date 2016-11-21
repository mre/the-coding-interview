<?php

function flatten($arr)
{
  $result = [];
  $queue = [$arr];

  while (count($queue) > 0)
  {
    $current = array_pop($queue);

    if (is_array($current))
    {
      foreach ($current as $element)
      {
        $queue[] = $element;
      }
    }
    else
    {
      $result[] = $current;
    }
  }
  return $result;
}

print_r(flatten([1,2,3])); // [1, 2, 3]
print_r(flatten([[1,2],3])); // [1, 2, 3]
print_r(flatten([[[1],2],3])); // [1, 2, 3]
