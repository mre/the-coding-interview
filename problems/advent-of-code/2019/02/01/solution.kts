#!/usr/bin/env kscript

println(args[0].split(',').map { it.toInt() }.toIntArray().also {
    var ip = 0
    while (it[ip] != 99) {
        when (it[ip]) {
            1 -> it[ip, 3] = it[ip, 1] + it[ip, 2]
            2 -> it[ip, 3] = it[ip, 1] * it[ip, 2]
            else -> error("Unknown opcode ${it[ip]}")
        }
        ip += 4
    }
}.joinToString(","))

operator fun IntArray.get(ip: Int, p: Int) =
    this[this[ip + p]]

operator fun IntArray.set(ip: Int, p: Int, v: Int) {
    this[this[ip + p]] = v
}
