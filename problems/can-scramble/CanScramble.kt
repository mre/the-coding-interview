import kotlin.test.assertFalse
import kotlin.test.assertTrue

fun main() {
    assertTrue("abc".canScramble("cba"))
    assertFalse("ac".canScramble("bb"))
    assertFalse("aab".canScramble("bba"))
}

private fun String.canScramble(other: String) =
    length == other.length && toScrambleMap() == other.toScrambleMap()

private fun String.toScrambleMap() =
    mutableMapOf<Char, Int>().also { forEach { c -> it.merge(c, 1, Int::plus) } }
