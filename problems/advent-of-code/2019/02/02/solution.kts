#!/usr/bin/env kscript

import kotlin.system.exitProcess

inline fun IntArray.apply(i: Int, op: (Int, Int) -> Int) {
    this[this[i + 3]] = op(this[this[i + 1]], this[this[i + 2]])
}

fun IntArray.computer(): Int {
    var i = 0
    while (this[i] != 99) {
        when (this[i]) {
            1 -> apply(i, Math::addExact)
            2 -> apply(i, Math::multiplyExact)
            else -> error("Unknown opcode ${this[i]}")
        }
        i += 4
    }
    return this[0]
}

val input = args[0].split(',').map { it.toInt() }.toIntArray()

(0..99).forEach { noun ->
    (0..99).forEach { verb ->
        if (input.copyOf().apply { set(1, noun); set(2, verb) }.computer() == 19690720) {
            println(100 * noun + verb)
            exitProcess(0)
        }
    }
}
exitProcess(1)
