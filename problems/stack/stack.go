package main

/*
An example of a stack being implemented in Go,
*/

import "fmt"

func main() {
	// Initalize the stack type
	stack := Stack{}

	stack.Show()              // Stack: []
	stack.Push(42)            // Adds to the stack, current stack = [42]
	stack.Push(23)            // Adds to the stack, current stack = [42 23]
	stack.Push(5)             // Adds to the stack, current stack = [42 23 5]
	fmt.Println(stack.Size()) // 3
	stack.Show()              // Stack: [42 23 5]
	fmt.Println(stack.Pop())  // 5
	stack.Show()              // Stack: [42 23]
	fmt.Println(stack.Pop())  // 23
	fmt.Println(stack.Size()) // 1
	stack.Show()              // Stack: [42]
	fmt.Println(stack.Pop())  // 42
	stack.Show()              // Stack: []
	fmt.Println(stack.Pop())  // panic: Attempt to pop an empty Stack!
}

// Struct to hold the stack items
type Stack struct {
	Items []int
}

// Show prints out the current stack
func (stack *Stack) Show() {
	fmt.Printf("Stack: %+v\n", stack.Items)
}

// Push adds an item to the current stack
func (stack *Stack) Push(item int) {
	stack.Items = append(stack.Items, item)
}

// Pop removes the last item from the stack
// fails if the stack is empty
func (stack *Stack) Pop() int {
	if !stack.IsEmpty() {
		poppedItem := stack.Items[len(stack.Items)-1]
		stack.Items = stack.Items[:len(stack.Items)-1]
		return poppedItem
	}
	panic("Attempt to pop an empty Stack!")
}

// Size returns the length of the current stack as int
func (stack *Stack) Size() int {
	return len(stack.Items)
}

// IsEmpty returns where the stack is empty or not as boolean
func (stack *Stack) IsEmpty() bool {
	return len(stack.Items) == 0
}
