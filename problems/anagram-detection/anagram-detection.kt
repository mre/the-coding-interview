private val charToPrime: Map<Char, Int> = mapOf(
    'a' to 2,
    'b' to 3,
    'c' to 5,
    'd' to 7,
    'e' to 11,
    'f' to 13,
    'g' to 17,
    'h' to 19,
    'i' to 23,
    'j' to 29,
    'k' to 31,
    'l' to 37,
    'm' to 41,
    'n' to 43,
    'o' to 47,
    'p' to 53,
    'q' to 59,
    'r' to 61,
    's' to 67,
    't' to 71,
    'u' to 73,
    'v' to 79,
    'w' to 83,
    'x' to 89,
    'y' to 97,
    'z' to 101,
    'A' to 103,
    'B' to 107,
    'C' to 109,
    'D' to 113,
    'E' to 127,
    'F' to 131,
    'G' to 137,
    'H' to 139,
    'I' to 149,
    'J' to 151,
    'K' to 163,
    'L' to 167,
    'M' to 173,
    'N' to 179,
    'O' to 181,
    'P' to 191,
    'Q' to 193,
    'R' to 197,
    'S' to 199,
    'T' to 211,
    'U' to 223,
    'V' to 227,
    'W' to 229,
    'X' to 233,
    'Y' to 239,
    'Z' to 241
)

fun String.hash(): Int = map { charToPrime[it] ?: error("Unmapped char $it") }.fold(1) { acc, v -> acc * v }

fun anagramDetection(parent: String, child: String): List<String> = buildList {
    when {
        parent.isEmpty() || child.isEmpty() || parent.length < child.length -> {}
        parent.length == child.length -> child.takeIf { parent.hash() == it.hash() }?.run(::add)
        else -> {
            val childHash: Int = child.hash()
            parent.windowed(child.length, 1)
                .filter { it.hash() == childHash }
                .run(::addAll)
        }
    }
}

check(anagramDetection("", "") == emptyList<String>())
check(anagramDetection("x", "foo") == emptyList<String>())
check(anagramDetection("foo", "bar") == emptyList<String>())
check(anagramDetection("AdnBndAndBdaBn", "dAn") == listOf("Adn", "ndA", "dAn", "And"))
