#!/usr/bin/env kscript

val amplifiers = 'A'..'E'
val inputRange = 0..4
val data = Container(args[0].split(',').map { it.toInt() }.toIntArray())

var max = Int.MIN_VALUE
inputRange.toList().toIntArray().forEachPermutation {
    max = maxOf(max, thrusterSignal(Container(it)))
}
println(max)

fun IntArray.forEachPermutation(action: (IntArray) -> Unit) {
    val indices = IntArray(size)
    action(this)
    var i = 0
    while (i < size) {
        if (indices[i] < i) {
            swap(if (i % 2 == 0) 0 else indices[i], i)
            action(this)
            ++indices[i]
            i = 0
        } else {
            indices[i] = 0
            ++i
        }
    }
}

fun IntArray.swap(a: Int, b: Int) {
    val tmp = this[a]
    this[a] = this[b]
    this[b] = tmp
}

fun thrusterSignal(input: Container): Int {
    var output = 0
    for (i in 0 until amplifiers.count()) {
        processing@ while (data.current() != 99) {
            val instruction = data.current()
            val mode = instruction / 100
            val opcode = instruction % 100

            data += when (opcode) {
                1 -> 4.also { data.apply(mode, Math::addExact) }
                2 -> 4.also { data.apply(mode, Math::multiplyExact) }
                3 -> 2.also { data[data.peek()] = if (i == input.i) input.next() else output }
                4 -> 2.also { output = data.peek(mode.isImmediate(1)) }
                5 -> if (data.peek(mode.isImmediate(1)) != 0) {
                    data.i = data.peek(mode.isImmediate(2), 2)
                    continue@processing
                } else 3
                6 -> if (data.peek(mode.isImmediate(1)) == 0) {
                    data.i = data.peek(mode.isImmediate(2), 2)
                    continue@processing
                } else 3
                7 -> 4.also { data.apply(mode) { a, b -> if (a < b) 1 else 0 } }
                8 -> 4.also { data.apply(mode) { a, b -> if (a == b) 1 else 0 } }
                else -> throw IllegalArgumentException("Unknown opcode $opcode: something went wrong")
            }
        }
        data.reset()
    }
    return output
}

fun Int.isImmediate(param: Int): Boolean =
    when (param) {
        1 -> 1
        2 -> 10
        3 -> 100
        else -> throw IllegalArgumentException("$param must be in [1..3]")
    }.let { (this and it) == it }

class Container(val value: IntArray, var i: Int = 0) {
    operator fun set(i: Int, n: Int) = value.set(i, n)
    operator fun plusAssign(x: Int) {
        i += x
    }

    fun current() = value[i]
    fun next() = value[i++]
    fun peek(x: Int = 1) = value[i + x]
    fun peek(immediate: Boolean, x: Int = 1) = peek(x).let { if (immediate) it else value[it] }
    fun reset() {
        i = 0
    }

    fun apply(mode: Int, op: (Int, Int) -> Int) {
        value[peek(3)] = op(
            peek(1).let { if (mode.isImmediate(1)) it else value[it] },
            peek(2).let { if (mode.isImmediate(2)) it else value[it] }
        )
    }
}
