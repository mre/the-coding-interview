#!/usr/bin/env kscript

import kotlin.math.abs

require(args.isNotEmpty()) { "Missing required input argument." }
require(args[0].isNotBlank()) { "Input must not be blank." }

val wires = args[0].trim().split('\n')
require(wires.size == 2) { "Expected exactly 2 wires, got: ${wires.size}" }

typealias E = Pair<Int, Int>

fun String.moves(): MutableList<E> = mutableListOf<E>().also {
    var x = 0
    var y = 0
    split(',').forEach { move ->
        val distance = move.substring(1).toInt()
        System.err.print("  ${move[0]}($distance) := ")
        when (move[0]) {
            'U' -> {
                for (i in (y + 1)..(y + distance)) {
                    it.add(E(x, i))
                }
                y += distance
            }
            'R' -> {
                for (i in (x + 1)..(x + distance)) {
                    it.add(E(i, y))
                }
                x += distance
            }
            'D' -> {
                for (i in (y - 1) downTo (y - distance)) {
                    it.add(E(x, i))
                }
                y -= distance
            }
            'L' -> {
                for (i in (x - 1) downTo (x - distance)) {
                    it.add(E(i, y))
                }
                x -= distance
            }
            else -> throw IllegalArgumentException("Invalid direction, got: ${move[0]}")
        }
    }
}

wires[0].moves().apply { retainAll(wires[1].moves()) }.map { (x, y) -> abs(x) + abs(y) }.min().also(::println)
