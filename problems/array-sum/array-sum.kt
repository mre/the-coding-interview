import java.util.Stack
import kotlin.test.assertEquals

data class IntListOrInt(val list: List<IntListOrInt>?, val int: Int?) {
    val isList = list != null
    val isInt = int != null
}

fun list(vararg values: IntListOrInt) = IntListOrInt(values.toList(), null)
fun int(value: Int) = IntListOrInt(null, value)

fun arraySum(vararg input: IntListOrInt): Int {
    var result = 0

    Stack<List<IntListOrInt>>().apply {
        push(input.toList())
        do {
            pop().forEach {
                when {
                    it.isList -> push(it.list!!)
                    it.isInt -> result += it.int!!
                }
            }
        } while (isNotEmpty())
    }

    return result
}

fun main(args: Array<String>) {
    assertEquals(15, arraySum(int(1), int(2), list(int(3), int(4), list(int(5)))))
}

// It is possible to solve the problem without defining a dedicated recursive
// type, however, the function parameter will be untyped and safety relies on
// runtime exceptions. The recursive type on the other hand ensures that the
// compiler can verify at compile time that everything is safe and sound.
//
// fun arraySum(input: List<Any>): Int {
//     var result = 0
//
//     Stack<List<*>>().apply {
//         push(input)
//         do {
//             pop().forEach {
//                 when (it) {
//                     is List<*> -> push(it)
//                     is Int -> result += it
//                     else -> throw IllegalArgumentException("element must be a List<*> or an Int")
//                 }
//             }
//         } while (isNotEmpty())
//     }
//
//     return result
// }
