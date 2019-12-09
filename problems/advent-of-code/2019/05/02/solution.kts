#!/usr/bin/env kscript

class Container(private val value: IntArray, var i: Int = 0) {
    operator fun get(i: Int) = value[i]
    operator fun set(i: Int, n: Int) = value.set(i, n)
    operator fun plusAssign(x: Int) { i += x }
    fun current() = value[i]
    fun next() = value[i++]
    fun peek(x: Int = 1) = value[i + x]
    fun peek(immediate: Boolean, x: Int = 1) = peek(x).let { if (immediate) it else value[it] }

    fun apply(mode: Int, op: (Int, Int) -> Int) {
        value[peek(3)] = op(
            peek(1).let { if (mode.isImmediate(1)) it else value[it] },
            peek(2).let { if (mode.isImmediate(2)) it else value[it] }
        )
    }
}

val (input, data) = args[0].trim().split('\n').map { line ->
    Container(line.split(',').map { it.toInt() }.toIntArray())
}

loop@ while (data.current() != 99) {
    val instruction = data.current()
    val mode = instruction / 100
    val opcode = instruction % 100

    data += when (opcode) {
        1 -> 4.also { data.apply(mode, Math::addExact) }
        2 -> 4.also { data.apply(mode, Math::multiplyExact) }
        3 -> 2.also { data[data.peek()] = input.next() }
        4 -> 2.also { println(data.peek(mode.isImmediate(1))) }
        5 -> if (data.peek(mode.isImmediate(1)) != 0) {
            data.i = data.peek(mode.isImmediate(2), 2)
            continue@loop
        } else 3
        6 -> if (data.peek(mode.isImmediate(1)) == 0) {
            data.i = data.peek(mode.isImmediate(2), 2)
            continue@loop
        } else 3
        7 -> 4.also { data.apply(mode) { a, b -> if (a < b) 1 else 0 } }
        8 -> 4.also { data.apply(mode) { a, b -> if (a == b) 1 else 0 } }
        else -> throw IllegalArgumentException("Unknown opcode $opcode: something went wrong")
    }
}

fun Int.isImmediate(param: Int): Boolean =
    when (param) {
        1 -> 1
        2 -> 10
        3 -> 100
        else -> throw IllegalArgumentException("$param must be in [1..3]")
    }.let { (this and it) == it }
