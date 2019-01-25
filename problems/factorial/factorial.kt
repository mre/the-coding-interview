fun factorial(n: Int): Int =
    when (n) {
        0, 1 -> 1
        else -> n * factorial(n - 1)
    }
