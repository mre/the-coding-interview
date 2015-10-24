<?php

function reverse($str) {
  $len = strlen($str);
  for ($i = 0; $i < $len/2; $i++)
  {
    $tmp = $str[$i];
    $str[$i] = $str[$len - $i -1];
    $str[$len - $i - 1] = $tmp;
  }
  return $str;
}

echo reverse("hello world"); // --> dlrow olleh
