#!/usr/bin/env kscript

import java.lang.Math.toIntExact as int

fun main(args: Array<String>) {
    val mem = args[0].split(',').map { it.toLong() }.toMutableList()
    val out = mutableListOf<Long>()
    var rb = 0
    var ip = 0

    do {
        when (val opcode = mem[ip] % 100) {
            1L -> {
                mem[ip, rb, 3] = Math.addExact(mem[ip, rb, 1], mem[ip, rb, 2])
                ip += 4
            }
            2L -> {
                mem[ip, rb, 3] = Math.multiplyExact(mem[ip, rb, 1], mem[ip, rb, 2])
                ip += 4
            }
            3L -> {
                mem[ip, rb, 1] = 2
                ip += 2
            }
            4L -> {
                out.add(mem[ip, rb, 1])
                ip += 2
            }
            5L -> {
                if (mem[ip, rb, 1] != 0L) ip = int(mem[ip, rb, 2])
                else ip += 3
            }
            6L -> {
                if (mem[ip, rb, 1] == 0L) ip = int(mem[ip, rb, 2])
                else ip += 3
            }
            7L -> {
                mem[ip, rb, 3] = if (mem[ip, rb, 1] < mem[ip, rb, 2]) 1 else 0
                ip += 4
            }
            8L -> {
                mem[ip, rb, 3] = if (mem[ip, rb, 1] == mem[ip, rb, 2]) 1 else 0
                ip += 4
            }
            9L -> {
                rb += int(mem[ip, rb, 1])
                ip += 2
            }
            99L -> {
                println(out.joinToString(","))
                return
            }
            else -> error("Unknown Opcode $opcode (ins=${mem[ip]}, ip=$ip)")
        }
    } while (true)
}

fun List<Long>.i(ip: Int, rb: Int, p: Int) =
    when (val mode = when (p) {
        1 -> this[ip] % 1000 / 100
        2 -> this[ip] % 10000 / 1000
        3 -> this[ip] / 10000
        else -> error("Unknown param $p")
    }) {
        0L -> int(this[ip + p])
        1L -> ip + p
        2L -> rb + int(this[ip + p])
        else -> error("Unknown mode $mode")
    }

operator fun List<Long>.get(ip: Int, rb: Int, p: Int) =
    getOrElse(i(ip, rb, p)) { 0 }

operator fun MutableList<Long>.set(ip: Int, rb: Int, p: Int, v: Long) {
    val i = i(ip, rb, p)
    if (i < size) {
        set(i, v)
    } else {
        if (i > size) addAll(Array(i - size) { 0L })
        add(v)
    }
}
