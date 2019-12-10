#!/usr/bin/env kscript

import kotlin.math.abs

const val ASTEROID = '#'

tailrec fun gcd(a: Int, b: Int): Int =
    if (a == 0) abs(b) else gcd(b % a, a)

typealias Asteroid = Pair<Int, Int>

val Asteroid.x get() = first
val Asteroid.y get() = second

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

    asteroids
        .map { a ->
            val inSight = mutableSetOf<Asteroid>()
            asteroids.forEach { b -> if (a != b) inSight.add((b - a).normalize()) }
            Triple(a.x, a.y, inSight.size)
        }
        .maxBy { it.inSight }!!
        .also { println("${it.x},${it.y} with ${it.inSight}") }
}
