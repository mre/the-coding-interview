import kotlin.test.assertFalse
import kotlin.test.assertTrue

fun String.canScramble(other: String) =
    length == other.length && chars().sum() == other.chars().sum()

fun main(args: Array<String>) {
    assertTrue("abc".canScramble("cba"))
    assertFalse("aab".canScramble("bba"))
}
