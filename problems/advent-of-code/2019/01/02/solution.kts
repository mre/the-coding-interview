#!/usr/bin/env kscript

println(args[0].lineSequence().map { it.toInt().fuel() }.sum())

tailrec fun Int.fuel(): Int =
    (this / 3 - 2).let { if (it < 1) 0 else it + it.fuel() }
