<?php

function intersection($a, $b)
{
  $output = [];
  foreach ($a as $elem)
  {
    if (in_array($elem, $b))
    {
      $output[] = $elem;
    }
  }
  return $output;
}

function intersection_hash($a, $b)
{
  $output = [];
  $tmp = [];
  foreach ($a as $elem)
  {
    $tmp[$elem] = True;
  }

  foreach ($b as $elem)
  {
    if (isset($tmp[$elem]))
    {
      $output[] = $elem;
    }
  }
  return $output;
}


var_dump(intersection(["bacon", "cake", "cheese"], ["smile", "laugh", "cheese"]));
var_dump(intersection_hash(["bacon", "cake", "cheese"], ["smile", "laugh", "cheese"]));
