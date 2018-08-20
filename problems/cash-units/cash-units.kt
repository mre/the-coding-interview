import kotlin.test.assertEquals

private val availableCashUnits = listOf(500_00, 200_00, 100_00, 50_00, 20_00, 10_00, 5_00, 2_00, 1_00, 50, 20, 10, 5, 2, 1)

fun Int.cashUnits(): Map<Int, Int> =
    LinkedHashMap<Int, Int>(availableCashUnits.size).also { result ->
        var rest = this
        for (cashUnit in availableCashUnits) {
            val n = rest / cashUnit
            result[cashUnit] = n
            rest %= cashUnit
        }
    }

fun main(args: Array<String>) {
    val expected = mapOf(
        500_00 to 3,
        200_00 to 2,
        100_00 to 0,
        50_00 to 1,
        20_00 to 1,
        10_00 to 0,
        5_00 to 0,
        2_00 to 1,
        1_00 to 0,
        50 to 1,
        20 to 1,
        10 to 0,
        5 to 1,
        2 to 1,
        1 to 1
    )

    assertEquals(expected, 1972_78.cashUnits())
}
