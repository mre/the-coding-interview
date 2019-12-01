#!/usr/bin/env kscript

fun isShuffle(a: String, b: String, c: String) =
    if ((a.length + b.length) != c.length) false else {
        var ai = 0
        var bi = 0
        c.forEach {
            when (it) {
                a.getOrNull(ai) -> ++ai
                b.getOrNull(bi) -> ++bi
                else -> return false
            }
        }
        true
    }

check(isShuffle("abc", "def", "dabecf"))
check(!isShuffle("bac", "def", "dabecf"))
check(isShuffle("otto", "anna", "oatntnoa"))
check(!isShuffle("otto", "anna", ""))
