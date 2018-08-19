import java.text.NumberFormat
import kotlin.test.assertEquals

private val metricPrefixes = listOf("K", "M", "G", "T", "P", "E", "Z", "Y")

fun <T> T.byteFormat(maximumFractionDigits: Int = 2): String where T : Number, T : Comparable<T> {
    var n = toDouble()
    var metricPrefix = ""

    for (prefix in metricPrefixes) {
        val x = n / 1024
        if (x < 1) break
        n = x
        metricPrefix = prefix
    }

    val nf = NumberFormat.getInstance()
    nf.maximumFractionDigits = maximumFractionDigits
    return "${nf.format(n)} ${metricPrefix}B"
}

fun main(args: Array<String>) {
    assertEquals("1 B", 1.byteFormat())
    assertEquals("12.5 B", 12.5.byteFormat())
    assertEquals("7.91 KB", 8101.byteFormat())
    assertEquals("12.042 KB", 12331.byteFormat(3))
    assertEquals("149.57 MB", 156833213.byteFormat())
}
