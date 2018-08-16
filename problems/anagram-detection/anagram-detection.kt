fun anagramDetection(parent: String, child: String): Int =
    when {
        parent.isEmpty() || child.isEmpty() || parent.length < child.length -> 0
        parent.length == child.length -> (parent.chars().sum() == child.chars().sum()).compareTo(false)
        else -> {
            val childSum = child.chars().sum()
            var result = 0
            var start = 0
            var end = child.length

            do {
                if (parent.substring(start, end).chars().sum() == childSum) {
                    ++result
                }
                ++start
                ++end
            } while (end < parent.length)

            result
        }
    }
