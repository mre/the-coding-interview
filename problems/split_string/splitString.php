<?php

function splitString($str, $delimiter)
{
  $chars = str_split($str);
  $words = [];
  $current = "";

  foreach($chars as $char)
  {
    if ($char === $delimiter)
    {
      $words[] = $current;
      $current = "";
    }
    else
    {
      $current .= $char;
    }
  }
  $words[] = $current;
  return $words;
}

var_dump(splitString("hello, world", ","));
var_dump(splitString("hello world", ","));
var_dump(splitString("", ","));
