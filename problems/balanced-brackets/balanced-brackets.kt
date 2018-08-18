import java.util.Stack
import kotlin.test.assertFalse
import kotlin.test.assertTrue

fun balancedBrackets(input: String, brackets: Map<Char, Char> = mapOf(']' to '[', ')' to '(', '}' to '{')) =
    Stack<Char>().apply {
        require(input.all { it in brackets.flatMap { (k, v) -> listOf(k, v) } })

        input.forEach {
            when {
                it in brackets.values -> push(it)
                isEmpty() || pop() != brackets[it] -> return false
            }
        }
    }.isEmpty()


fun main(args: Array<String>) {
    assertTrue(balancedBrackets("()[]{}(([])){[()][]}"))
    assertFalse(balancedBrackets("())[]{}"))
    assertFalse(balancedBrackets("[(])"))
}
