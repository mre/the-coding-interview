#!/usr/bin/env kscript

args[0].split(',').also { (w, h, data) ->
    data.chunked(w.toInt() * h.toInt()).minBy { it.count('0') }!!.also {
        println(it.count('1') * it.count('2'))
    }
}

fun String.count(c: Char) = count { it == c }
