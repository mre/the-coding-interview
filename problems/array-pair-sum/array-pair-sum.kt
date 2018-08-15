fun arrayPairSum(k: Int, values: List<Int>): List<Pair<Int, Int>> =
    mutableListOf<Pair<Int, Int>>().apply {
        values.forEachIndexed { i, x ->
            values.listIterator(i + 1).forEach { y ->
                if (x + y == k) add(x to y)
            }
        }
    }
