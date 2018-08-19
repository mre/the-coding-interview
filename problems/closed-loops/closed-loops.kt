import kotlin.test.assertEquals

fun Int.loops() =
    toString().fold(0) { acc, c ->
        acc + when (c) {
            '0', '6', '9' -> 1
            '8' -> 2
            else -> 0
        }
    }

fun main(args: Array<String>) {
    assertEquals(3, 2876.loops())
    assertEquals(2, 2581.loops())
    assertEquals(4, 10000.loops())
    assertEquals(4, 16789.loops())
}
