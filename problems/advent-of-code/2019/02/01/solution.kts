#!/usr/bin/env kscript

inline fun IntArray.apply(i: Int, op: (Int, Int) -> Int) {
    this[this[i + 3]] = op(this[this[i + 1]], this[this[i + 2]])
}

val data = args[0].split(',').map { it.toInt() }.toIntArray()

var i = 0
while (data[i] != 99) {
    when (data[i]) {
        1 -> data.apply(i, Math::addExact)
        2 -> data.apply(i, Math::multiplyExact)
        else -> throw IllegalArgumentException("Unknown opcode ${data[i]}: something went wrong")
    }
    i += 4
}

println(data.joinToString(","))
