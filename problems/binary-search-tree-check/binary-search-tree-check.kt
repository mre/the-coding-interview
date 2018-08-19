import java.util.Stack
import kotlin.test.assertFalse
import kotlin.test.assertTrue

class TreeStack<T : Comparable<T>>(treeNode: TreeNode<T>) : Stack<Triple<TreeNode<T>, T?, T?>>() {
    init {
        push(treeNode)
    }

    inline fun drain(action: TreeStack<T>.(node: TreeNode<T>, min: T?, max: T?) -> Unit) {
        while (isNotEmpty()) pop().also { (node, min, max) -> action(node, min, max) }
    }

    fun push(node: TreeNode<T>, min: T? = null, max: T? = null) = apply {
        push(Triple(node, min, max))
    }
}

data class TreeNode<T : Comparable<T>>(
    val value: T,
    val left: TreeNode<T>? = null,
    val right: TreeNode<T>? = null
) {
    fun isBalancedBinarySearchTree(duplicates: Boolean = false): Boolean {
        if (!(left == null && right == null)) {
            TreeStack(this).drain { node, min, max ->
                min?.let { if (it >= node.value) return false }
                max?.let { if ((!duplicates && it == node.value) || it < node.value) return false }
                node.left?.let { push(it, max = node.value) }
                node.right?.let { push(it, min = node.value) }
            }
        }
        return true
    }
}

fun main(args: Array<String>) {
    assertTrue(TreeNode(1).isBalancedBinarySearchTree())
    assertTrue(TreeNode(2, TreeNode(1)).isBalancedBinarySearchTree())
    assertTrue(TreeNode(2, right = TreeNode(3)).isBalancedBinarySearchTree())

    assertFalse(TreeNode(4, TreeNode(4)).isBalancedBinarySearchTree())
    assertTrue(TreeNode(4, TreeNode(4)).isBalancedBinarySearchTree(duplicates = true))

    // right node cannot be equal to parent
    assertFalse(TreeNode(4, right = TreeNode(4)).isBalancedBinarySearchTree(duplicates = true))

    // degenerated trees are still balanced
    assertTrue(TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1)))).isBalancedBinarySearchTree())

    TreeNode(
        300,
        TreeNode(
            200,
            TreeNode(100, TreeNode(50), TreeNode(150)),
            TreeNode(250, right = TreeNode(275))
        ),
        TreeNode(
            400,
            TreeNode(350),
            TreeNode(500, TreeNode(450), TreeNode(600))
        )
    ).apply { assertTrue(isBalancedBinarySearchTree()) }
}
