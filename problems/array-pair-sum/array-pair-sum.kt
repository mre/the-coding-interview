import kotlin.math.max
import kotlin.math.min
import kotlin.test.assertEquals

fun arrayPairSum(k: Int, values: List<Int>): List<Pair<Int, Int>> {
    val seen = mutableSetOf<Long>()

    return values.asSequence().map(Int::toLong).fold(mutableListOf()) { result, current ->
        val target = k - current
        if (target in seen) result.add(min(current, target).toInt() to max(current, target).toInt())
        else seen.add(current)
        result
    }
}

fun main(args: Array<String>) {
    assertEquals(
        listOf(4 to 6, 3 to 7),
        arrayPairSum(10, listOf(3, 4, 5, 6, 7))
    )

    assertEquals(
        listOf(3 to 5, 4 to 4, 4 to 4),
        arrayPairSum(8, listOf(3, 4, 5, 4, 4))
    )
}
