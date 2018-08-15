import java.util.Stack

fun arraySum(input: List<Any>): Int {
    var result = 0

    Stack<List<*>>().apply {
        push(input)
        do {
            pop().forEach {
                when (it) {
                    is List<*> -> push(it)
                    is Int -> result += it
                    else -> throw IllegalArgumentException("element must be a List<*> or an Int")
                }
            }
        } while (isNotEmpty())
    }

    return result
}
