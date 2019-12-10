#!/usr/bin/env kscript

println(args[0].lineSequence().map { it.toInt() / 3 - 2 }.sum())
