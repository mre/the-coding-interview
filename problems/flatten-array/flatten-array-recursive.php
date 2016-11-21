<?php

function flatten($arr)
{
  $result = [];

  foreach ($arr as $current)
  {
    if (is_array($current))
    {
      $result = array_merge($result, flatten($current));
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
