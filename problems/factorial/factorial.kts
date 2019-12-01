#!/usr/bin/env kscript

fun loop(n: ULong): ULong =
    if (n <= 1uL) 1uL else {
        var acc = 1uL
        var x = n
        do {
          acc *= x
        } while (--x > 1uL)
        acc
    }

fun reduce(n: ULong): ULong =
    if (n <= 1uL) 1uL else (1uL..n).reduce { acc, x -> acc * x }

// https://kotlinlang.org/docs/reference/functions.html#tail-recursive-functions
tailrec fun recursive(n: ULong): ULong =
    if (n <= 1uL) 1uL else n * recursive(n - 1uL)

arrayOf(::loop, ::reduce, ::recursive).forEach {
    check(it(0uL) == 1uL)
    check(it(1uL) == 1uL)
    check(it(2uL) == 2uL)
    check(it(3uL) == 6uL)
    check(it(4uL) == 24uL)
    check(it(5uL) == 120uL)
    check(it(20uL) == 2_432_902_008_176_640_000uL)
}
