#!/usr/bin/env php
<?php

$z = ord('z');
$a = ord('a');
$s = $argv[1];
$l = strlen($argv[1]);
for ($i = 0; $i < $l; ++$i) {
    echo $s[$i] === "\n" ? "\n" : chr($z - (ord($s[$i]) - $a));
}
