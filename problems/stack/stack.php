<?php

class Stack {

  public function __construct()
  {
    $this->stack = [];
  }

  public function push($val)
  {
    $this->stack[] = $val;
  }

  public function pop()
  {
    return array_pop($this->stack);
  }

  public function length()
  {
    return count($this->stack);
  }

  public function isEmpty()
  {
    return count($this->stack) === 0;
  }
}


$s = new Stack();
assert($s->isEmpty());
assert($s->length() === 0);
$s->push("hello");
assert($s->length() === 1);
$s->push("world");
assert($s->length() === 2);
$v = $s->pop();
assert($v === "world");
assert($s->length() === 1);
$v = $s->pop();
assert($v === "hello");
assert($s->length() === 0);
assert($s->isEmpty());
