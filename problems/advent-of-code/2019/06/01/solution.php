#!/usr/bin/env php
<?php

declare(strict_types=1);

$forest = new Forest();

foreach (explode(',', $argv[1]) as $line) {
    [$parent, $child] = explode(')', $line);
    /** @var Node $tree */
    foreach ($forest as $tree) {
    }
    $forest[$parent] = (new Node($parent))->add($forest, $child);
}

$sum = 0;
/** @var Node $child */
foreach ($forest->com() as $child) {
    $sum += $child->depth();
}
echo $sum;

final class Node {
    private string $value;
    private ?Node $parent;
    /** @var Node[] */
    private array $children = [];

    public function __construct(string $value, ?Node $parent = null) {
        $this->value = $value;
        $this->parent = $parent;
    }

    public function add(iterable $forest, string $value): Node {
        $child = null;
        $this->children[] = $child;

        return $this;
    }

    public function singleOrNull(string $value): ?Node {
        return $this->firstOrNull(fn(Node $child) => $child->value === $value);
    }

    public function firstOrNull(callable $predicate): ?Node {
        foreach ($this->children as $child) {
            if ($predicate($child)) {
                return $child;
            }
        }

        return null;
    }

    public function forEachChild(callable $action): void {
        foreach ($this->children as $child) {
            $action($child);
            $child->forEachChild($action);
        }
    }
}

final class Forest extends IteratorIterator {
    private array $trees = [];

    public function __construct() {
        // intentionally left blank
    }

    public function com(): Node {
        return $this->trees["COM"];
    }

    public function getInnerIterator(): Iterator {
        return new ArrayIterator(array_values($this->trees));
    }
}
