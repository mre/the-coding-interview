#!/usr/bin/env kscript

val input = args[0].substringBefore('\n').toInt()
val data = args[0].substringAfter('\n').split(',').map { it.toInt() }.toIntArray()
var i = 0

while (data[i] != 99) {
    val mode = data[i] / 100
    i += when (data[i] % 100) {
        1 -> 4.also { }
        2 -> 4.also { }
        3 -> 2.also { data[data[i + 1]] = input }
        4 -> 2.also { }
        else -> throw IllegalArgumentException(data[i].toString())
    }
}

Instructions(data).forEach {
    when (it.opcode) {
        1 -> 4.also {}
        2 -> 4.also {}
        3 -> 2.also {}
        4 -> 2.also {}
        else -> throw IllegalArgumentException("$it")
    }
}

class Instructions(private val value: IntArray) : Iterator<Instruction> {
    private var i = 0

    fun current() = value[i]

    operator fun set(x: Int, n: Int) {
        value[value[i + x]] = n
    }

    override fun hasNext() = value[i] != 99
    override fun next() = Instruction(value[i])
}

data class Instruction(val mode: Int, val opcode: Int) {
    constructor(value: Int) : this(value / 100, value % 100)
}

/*

class Container(private val value: IntArray, var i: Int = 0) {
    operator fun get(i: Int) = value[i]
    operator fun set(i: Int, n: Int) = value.set(i, n)
    operator fun plusAssign(x: Int) {
        i += x
    }

    fun current() = value[i]
    fun next() = value[i++]
    fun peek(x: Int = 1) = value[i + x]

    fun apply(mode: String, op: (Int, Int) -> Int) {
        value[peek(3)] = op(
            peek(1).let { if (mode[2] == '1') it else value[it] },
            peek(2).let { if (mode[1] == '1') it else value[it] }
        )
    }
}

while (data.current() != 99) {
    data.current().toString().padStart(5, '0').let { instruction ->
        val mode = instruction.substring(0, 3)
        val opcode = instruction.substring(3, 5)
        data += when (opcode) {
            "01" -> 4.also { data.apply(mode, Math::addExact) }
            "02" -> 4.also { data.apply(mode, Math::multiplyExact) }
            "03" -> 2.also { data[data.peek()] = input.next() }
            "04" -> 2.also { println(data.peek().let { if (mode[2] == '1') it else data[it] }) }
            else -> throw IllegalArgumentException("Unknown opcode $opcode: something went wrong")
        }
    }
}
