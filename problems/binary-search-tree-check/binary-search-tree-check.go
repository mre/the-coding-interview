package main

import (
	"fmt"
	"math"
)

func main() {
	// create NON BST
	node1 := Node{
		data: 1,
	}
	node4 := Node{
		data: 4,
	}
	node2 := Node{
		data:  2,
		left:  &node1,
		right: &node4,
	}
	node5 := Node{
		data: 5,
	}
	node3 := Node{
		data:  3,
		left:  &node2,
		right: &node5,
	}
	fmt.Println(isBST(&node3, math.MinInt64, math.MaxInt64))

	// create BST
	root := Node{
		data: 3,
	}
	insertNodeIntoBST(&root, 2)
	insertNodeIntoBST(&root, 5)
	insertNodeIntoBST(&root, 1)
	insertNodeIntoBST(&root, 4)
	fmt.Println(isBST(&root, math.MinInt64, math.MaxInt64))
}

type Node struct {
	data  int
	left  *Node
	right *Node
}

func insertNodeIntoBST(root *Node, data int) {
	if data < root.data {
		if root.left == nil {
			root.left = &Node{
				data: data,
			}
			return
		}

		insertNodeIntoBST(root.left, data)
		return
	}

	if root.right == nil {
		root.right = &Node{
			data: data,
		}
		return
	}

	insertNodeIntoBST(root.right, data)
}

func isBST(node *Node, min int, max int) bool {
	if node == nil {
		return true
	}

	if min > node.data || node.data > max {
		return false
	}

	return isBST(node.left, min, node.data) && isBST(node.right, node.data, max)
}
