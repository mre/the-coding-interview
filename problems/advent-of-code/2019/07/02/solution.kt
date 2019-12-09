#!/usr/bin/env kscript

//DEPS org.jetbrains.kotlinx:kotlinx-coroutines-core:1.3.2

import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.channels.ReceiveChannel
import kotlinx.coroutines.channels.SendChannel
import kotlinx.coroutines.coroutineScope
import kotlinx.coroutines.launch
import java.util.Collections

suspend fun main(args: Array<String>) {
    val (range, data) = args[0].split('\n').map { it.split(',').map { i -> i.toInt() }.toIntArray() }

    (range.first()..range.last()).permutations()
        .asIterable()
        .mapNotNull { settings ->
            coroutineScope {
                val channels = settings.map { Channel<Int>(Channel.UNLIMITED).apply { send(it) } }
                channels.first().send(0)
                channels.zipWithNext { input, output -> launch { compute(data, input, output) } }
                compute(data, channels.last(), channels.first())
            }
        }
        .max()
        .also(::println)
}

suspend fun IntRange.permutations(): Sequence<List<Int>> = sequence {
    val elements = toMutableList()
    val n = elements.size
    val indices = IntArray(n)
    var i = 0

    yield(elements)
    while (i < n) {
        if (indices[i] < i) {
            Collections.swap(elements, if (i and 1 == 0) 0 else indices[i], i)
            yield(elements)
            indices[i]++
            i = 0
        } else {
            indices[i] = 0
            i++
        }
    }
}

typealias InstructionPointer = Int
typealias Param = Int

const val P1: Param = 0b1
const val P2: Param = 0b10
const val P3: Param = 0b11

fun IntArray.i(ip: InstructionPointer, p: Param) =
    if ((this[ip] / 100) and p == p) ip + p
    else this[ip + p]

operator fun IntArray.get(ip: InstructionPointer, p: Param) =
    this[i(ip, p)]

operator fun IntArray.set(ip: InstructionPointer, p: Param, v: Int) {
    this[i(ip, p)] = v
}

suspend fun compute(data: IntArray, input: ReceiveChannel<Int>, output: SendChannel<Int>): Int? {
    val mem = data.copyOf()
    var result: Int? = null
    var ip: InstructionPointer = 0
    do {
        when (mem[ip] % 100) {
            1 -> {
                mem[ip, P3] = Math.addExact(mem[ip, P1], mem[ip, P2])
                ip += 4
            }
            2 -> {
                mem[ip, P3] = Math.multiplyExact(mem[ip, P1], mem[ip, P2])
                ip += 4
            }
            3 -> {
                mem[ip, P1] = input.receive()
                ip += 2
            }
            4 -> {
                output.send(mem[ip, P1].also { result = it })
                ip += 2
            }
            5 -> {
                if (mem[ip, P1] != 0) ip = mem[ip, P2]
                else ip += 3
            }
            6 -> {
                if (mem[ip, P1] == 0) ip = mem[ip, P2]
                else ip += 3
            }
            7 -> {
                mem[ip, P3] = if (mem[ip, P1] < mem[ip, P2]) 1 else 0
                ip += 4
            }
            8 -> {
                mem[ip, P3] = if (mem[ip, P1] == mem[ip, P2]) 1 else 0
                ip += 4
            }
            99 -> return result
            else -> error("Unknown Opcode ${mem[ip] % 100}")
        }
    } while (true)
}
