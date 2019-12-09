#!/usr/bin/env kscript

val forest = Forest()

args[0].lineSequence().map { it.split(')') }.forEach line@{ (parent, child) ->
    forest.forEach { tree ->
        if (null != (tree.takeIf { it.value == parent } ?: tree.singleOrNull(parent))?.add(forest, child)) {
            return@line
        }
    }
    forest.add(Node(parent).add(forest, child))
}

var sum = 0
forest.single { it.value == "COM" }.forEachChild { sum += it.depth() }
println(sum)

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

    fun forEachChild(action: (Node) -> Unit) {
        children.forEach {
            action(it)
            it.forEachChild(action)
        }
    }

    fun depth() = if (parent == null) 0 else {
        var transfers = 0
        var current = parent
        while (current != null) {
            ++transfers
            current = current.parent
        }
        transfers
    }

    override fun equals(other: Any?) = value == (other as? Node)?.value
    override fun hashCode() = value.hashCode()
}
