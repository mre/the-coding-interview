#!/usr/bin/env kscript

args[0].split(',').also {
    val width = it[0].toInt()
    val height = it[1].toInt()
    val layers = it[2].chunked(width * height)

    print(buildString {
        for (row in 0 until height) {
            for (cell in 0 until width) {
                val i = cell + (row * width)
                for (layer in layers) {
                    if (layer[i] in '0'..'1') {
                        append(if (layer[i] == '0') ' ' else '\u2588')
                        break
                    }
                }
            }
            append('\n')
        }
    })
}
