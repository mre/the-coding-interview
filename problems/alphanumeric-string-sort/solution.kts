#!/usr/bin/env kscript

import java.lang.StringBuilder

val parts = Array(4, ::StringBuilder)

args[0].toCharArray().sortedArray().forEach {
    parts[when (it) {
        in 'a'..'z' -> 0
        in 'A'..'Z' -> 1
        '0', '2', '4', '6', '8' -> 2
        else -> 3
    }].append(it)
}

parts.reduce { acc, it -> acc.append(it) }.also(::println)
