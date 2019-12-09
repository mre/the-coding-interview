#!/usr/bin/env kscript

println(args[0].splitToSequence('\n').map { Math.floorDiv(it.toInt(), 3) - 2 }.sum())
