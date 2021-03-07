class SynchronizedObject {
    @Synchronized fun sayHello(other: SynchronizedObject) {
        println("Hello!")
        other.sayHelloBack() // here, the deadlock happens!
    }
    @Synchronized fun sayHelloBack() {
        throw RuntimeException("this solution sucks!") // must not be executed!
    }
}

class DeadlockThread(val first: SynchronizedObject, val second: SynchronizedObject): Thread() {
    override fun run() {
        first.sayHello(second)
    }
}

fun main() {
    val firstObject = SynchronizedObject()
    val secondObject = SynchronizedObject()

    // joining the first thread before starting the other makes it safe!
    DeadlockThread(firstObject, secondObject).start()
    DeadlockThread(secondObject, firstObject).start()
}
