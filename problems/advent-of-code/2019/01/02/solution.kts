#!/usr/bin/env kscript

println(args[0].splitToSequence('\n').map {
    var sum = 0
    var x = it.toInt()
    while (x > 0) {
        x = maxOf(0, Math.floorDiv(x, 3) - 2)
        sum += x
    }
    sum
}.sum())
