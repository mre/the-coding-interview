import kotlin.test.assertEquals

private val cashUnits = listOf(50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)

fun Int.cashUnits(): Map<Int, Int> =
    cashUnits.associate { it to 0 }.toMutableMap().also { result ->
        var rest = this
        for (cashUnit in cashUnits) {
            (rest / cashUnit).takeIf { it > 0 }?.let {
                result[cashUnit] = it
                rest %= cashUnit
            }
        }
    }

fun main(args: Array<String>) {
    val expected = mapOf(
        50000 to 3,
        20000 to 2,
        10000 to 0,
        5000 to 1,
        2000 to 1,
        1000 to 0,
        500 to 0,
        200 to 1,
        100 to 0,
        50 to 1,
        20 to 1,
        10 to 0,
        5 to 1,
        2 to 1,
        1 to 1
    )

    assertEquals(expected, 197278.cashUnits())
}
