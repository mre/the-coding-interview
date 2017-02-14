<?php

function arraySum($arr)
{
  $sum = 0;
  foreach ($arr as $item)
  {
    if (is_array($item))
    {
      $sum += arraySum($item);
    }
    else
    {
      $sum += $item;
    }
  }
  return $sum;
}

var_dump(arraySum([1,2,[3,4,[5]]]));
