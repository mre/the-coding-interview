fun alphanumericStringSort(input: String): String {
    val parts = Array<MutableList<Char>>(4) { mutableListOf() }

    input.forEach {
        when (it) {
            in 'a'..'z' -> parts[0]
            in 'A'..'Z' -> parts[1]
            in '0'..'9' -> if (it.toInt().and(1) == 0) parts[2] else parts[3]
            else -> throw IllegalArgumentException("input must be alphanumeric")
        }.add(it)
    }

    return buildString {
        parts.forEach {
            it.sort()
            append(it.joinToString(""))
        }
    }
}
