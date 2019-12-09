#!/usr/bin/env kscript

import kotlin.math.abs

require(args.isNotEmpty()) { "Missing required input argument." }
require(args[0].isNotBlank()) { "Input must not be blank." }
val wires = args[0].trim().split('\n')

typealias E = Triple<Int, Int, Int>
fun String.toCoordinates(): List<E> =
    mutableListOf<E>().also {
        var x = 0
        var y = 0
        var z = 0
        split(',').forEach { move ->
            val distance = move.substring(1).toInt()
            when (move[0]) {
                'U' -> {
                    for (i in (y + 1)..(y + distance)) {
                        it.add(E(x, i, ++z))
                    }
                    y += distance
                }
                'R' -> {
                    for (i in (x + 1)..(x + distance)) {
                        it.add(E(i, y, ++z))
                    }
                    x += distance
                }
                'D' -> {
                    for (i in (y - 1) downTo (y - distance)) {
                        it.add(E(x, i, ++z))
                    }
                    y -= distance
                }
                'L' -> {
                    for (i in (x - 1) downTo (x - distance)) {
                        it.add(E(i, y, ++z))
                    }
                    x -= distance
                }
                else -> throw IllegalArgumentException(
                    "Invalid direction, got: ${move[0]}"
                )
            }
        }
    }

require(wires.size == 2) { "Expected exactly 2 wires, got: ${wires.size}" }

val a = wires[0].toCoordinates()
val b = wires[1].toCoordinates()
val c = a.mapNotNull { (ax, ay, az) ->
    b.firstOrNull { (bx, by) -> ax == bx && ay == by }?.let { E(ax, ay, az + it.third) }
}

println(c.map { (x, y, z) -> z to (abs(x) + abs(y)) }.minWith(Comparator { (az, an), (bz, bn) ->
    when {
        az == bz -> an.compareTo(bn)
        az < bz -> -1
        else -> 1
    }
})!!.first)
