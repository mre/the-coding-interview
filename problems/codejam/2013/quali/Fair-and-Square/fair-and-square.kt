import java.io.File
import java.text.NumberFormat
import kotlin.math.sqrt
import kotlin.test.assertEquals

val nf: NumberFormat = NumberFormat.getInstance()

inline val Number.isPalindrome get() = nf.format(this).let { it == it.reversed() }

inline val Number.square get() = sqrt(toDouble())

fun IntRange.fairAndSquare() =
    fold(0) { acc, i -> acc + if (i.isPalindrome && i.square.isPalindrome) 1 else 0 }

fun main(args: Array<String>) {
    val dir = File(args.firstOrNull() ?: ".")
    val input = File("$dir/C-small-practice.in").readLines()
    val output = File("$dir/C-small-practice.out").readLines().map { it.split(' ', limit = 3).last().toInt() }

    for (i in 1..input.first().toInt()) {
        input[i].split(' ', limit = 2).let { it[0].toInt()..it[1].toInt() }.fairAndSquare().let {
            val message = "Case #$i: $it"
            assertEquals(output[i - 1], it, message)
            println(message)
        }
    }
}
