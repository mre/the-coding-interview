#!/usr/bin/env kscript

val (parent, child) = args[0].trim().split('\n')
val parentLen = parent.length
val childLen = child.length

if (parentLen == childLen) {
    println((parent.chars().sum() == child.chars().sum()).compareTo(false))
} else {
    val childSum = child.chars().sum()
    var result = 0
    var start = 0
    var end = childLen

    do {
        if (parent.substring(start, end).chars().sum() == childSum) {
            ++result
        }
        ++start
        ++end
    } while (end < parentLen)

    println(result)
}
