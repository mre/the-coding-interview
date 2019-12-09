#!/usr/bin/env kscript

val (start, end) = args[0].split('-').map { it.toInt() }

var result = 0
loop@ for (i in start..end) {
    val chars = i.toString().toCharArray()

    val pairs = Array(chars.size - 1) { chars[it] to chars[it + 1] }
    if (pairs.none { pair -> pair.first == pair.second && pairs.filter { pair == it }.size == 1 }) {
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
