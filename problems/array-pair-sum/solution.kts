#!/usr/bin/env kscript

import kotlin.math.max
import kotlin.math.min

val input = args[0].splitToSequence(',').map { it.toInt() }
val k = input.first()
val pairs = mutableListOf<Pair<Int, Int>>()
val seen = mutableSetOf<Int>()
input.drop(1).forEach { n ->
    val x = k - n
    if (x != n) {
        if (x in seen) pairs.add(min(x, n) to max(x, n))
        else seen.add(n)
    }
}
println(pairs)
