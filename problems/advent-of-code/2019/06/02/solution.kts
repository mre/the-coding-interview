#!/usr/bin/env kscript

import kotlin.system.exitProcess

val forest = Forest()

args[0].lineSequence().map { it.split(')') }.forEach line@{ (parent, child) ->
    forest.forEach { tree ->
        if (null != (tree.takeIf { it.value == parent } ?: tree.singleOrNull(parent))?.add(forest, child)) {
            return@line
        }
    }
    forest.add(Node(parent).add(forest, child))
}

val com = forest.single { it.value == "COM" }
val you = com.single("YOU")
val san = com.single("SAN")

you.forEachParent { a ->
    san.forEachParent { b ->
        if (a == b) {
            println(you.depth() + san.depth() - 2 - (a.depth() * 2))
            exitProcess(0)
        }
    }
}
exitProcess(1)

typealias Forest = LinkedHashSet<Node>

class Node(val value: String, private var parent: Node? = null) {
    private val children = Forest()

    fun add(forest: Forest, value: String) = apply {
        val child = forest.firstOrNull { it.value == value }?.also { it.parent = this } ?: Node(value, this)
        children.add(child)
        forest.remove(child)
    }

    fun singleOrNull(value: String): Node? =
        children.mapNotNull { if (it.value == value) it else it.singleOrNull(value) }.singleOrNull()

    fun single(value: String) =
        singleOrNull(value) ?: throw NoSuchElementException("No $value in ${this.value}")

    fun forEachParent(action: (Node) -> Unit) {
        var current = parent
        while (current != null) {
            action(current)
            current = current.parent
        }
    }

    fun depth() = if (parent == null) 0 else {
        var transfers = 0
        forEachParent { ++transfers }
        transfers
    }

    override fun equals(other: Any?) = value == (other as? Node)?.value
    override fun hashCode() = value.hashCode()
}
