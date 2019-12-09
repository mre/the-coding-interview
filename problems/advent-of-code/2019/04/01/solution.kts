#!/usr/bin/env kscript

import kotlin.math.min

val (start, end) = args[0].split('-').map { it.toInt() }

var result = 0
loop@ for (i in start..end) {
    val chars = i.toString().toCharArray()

    if (chars.toSet().size == chars.size) {
        continue
    }

    var min = chars[0]
    for (j in 1 until chars.size) {
        val c = chars[j]
        if (c < min) continue@loop
        min = c
    }

    ++result
}
println(result)
