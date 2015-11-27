<?php

function arrayPairSum($k, $aValues)
{
  $aSeen = [];
  $aPairs = [];
  foreach ($aValues as $i)
  {
    $j = $k - $i;
    if (isset($aSeen[$j]))
    {
      $aPairs[] = [$i, $j];
    }
    else
    {
      $aSeen[$i] = true;
    }
  }
  return $aPairs;
}

print_r(arrayPairSum(10, [3,1,2,4,5,8,12,10,9,5]));
