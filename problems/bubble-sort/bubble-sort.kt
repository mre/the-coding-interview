import kotlin.test.assertEquals

fun <E : Comparable<E>> MutableList<E>.bubbleSort(): MutableList<E> =
    if (size < 2) this else apply {
        for (i in 0 until size)
            for (j in (i + 1) until size)
                if (this[i] > this[j]) {
                    val a = get(i)
                    val b = get(j)
                    set(i, b)
                    set(j, a)
                }
    }

fun <E : Comparable<E>> List<E>.bubbleSorted(): List<E> =
    ArrayList<E>(this).bubbleSort()

fun main(args: Array<String>) {
    assertEquals(listOf(1), listOf(1).bubbleSorted())
    assertEquals(listOf(1, 2), listOf(2, 1).bubbleSorted())
    assertEquals(listOf(1, 2, 3), listOf(2, 3, 1).bubbleSorted())
    assertEquals(listOf(1, 2, 4, 5, 8), listOf(5, 1, 4, 2, 8).bubbleSorted())
}
