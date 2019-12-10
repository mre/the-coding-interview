#!/usr/bin/env kscript

import java.util.ArrayDeque
import kotlin.math.abs
import kotlin.math.atan2

const val ASTEROID = '#'

tailrec fun gcd(a: Int, b: Int): Int =
    if (a == 0) abs(b) else gcd(b % a, a)

typealias Asteroid = Pair<Int, Int>

val Asteroid.x get() = first
val Asteroid.y get() = second

fun Asteroid.manhattanDistanceTo(other: Asteroid) =
    abs(x - other.x) + abs(y - other.y)

operator fun Asteroid.minus(other: Asteroid) =
    (x - other.x) to (y - other.y)

fun Asteroid.normalize() =
    gcd(x, y).let { (x / it) to (y / it) }

val Triple<Int, Int, Int>.x get() = first
val Triple<Int, Int, Int>.y get() = second
val Triple<Int, Int, Int>.inSight get() = third

fun main(args: Array<String>) {
    val asteroids = mutableListOf<Asteroid>()
    args[0].lineSequence().forEachIndexed { y, line ->
        line.forEachIndexed { x, c -> if (c == ASTEROID) asteroids.add(x to y) }
    }

    val best = asteroids.map { a ->
        val inSight = mutableSetOf<Asteroid>()
        asteroids.forEach { b -> if (a != b) inSight.add((b - a).normalize()) }
        Triple(a.x, a.y, inSight.size)
    }.maxBy { it.inSight }!!.let { it.x to it.y }

    val vaporMap = mutableMapOf<Asteroid, MutableList<Asteroid>>()

    asteroids.asSequence().filter { it != best }.forEach {
        vaporMap.getOrPut((it - best).normalize()) { mutableListOf() }.add(it)
    }

    vaporMap.mapValues { (_, v) ->
        v.sortBy { best.manhattanDistanceTo(it) }
    }

    val vaporSet = vaporMap.entries.sortedBy {
        -atan2(it.key.x.toDouble(), it.key.y.toDouble())
    }

    sequence<Asteroid> {
        val vaporQueue = ArrayDeque<ListIterator<Asteroid>>()
        vaporSet.forEach {
            vaporQueue.add(it.value.listIterator())
        }
        while (vaporQueue.isNotEmpty()) {
            val vaporize = vaporQueue.remove()
            yield(vaporize.next())
            if (vaporize.hasNext()) vaporQueue.add(vaporize)
        }
    }.elementAt(199).let { println(it.x * 100 + it.y) }
}
