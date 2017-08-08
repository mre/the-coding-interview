package main

import "fmt"

func main() {
	fmt.Println("=== Bubblesort ===")
	fmt.Println(bubblesort([]int{8, 2, 4, 7, 9, 0, 1, 4, 5, 7, 8, 9}))
	fmt.Println(bubblesort([]int{}))
	fmt.Println(bubblesort([]int{1}))
	fmt.Println(bubblesort([]int{1, 3}))
}

func bubblesort(list []int) []int {
	last := len(list) - 1
	for i := 0; i < last; i++ {
		for j := i + 1; j < last; j++ {
			if list[i] > list[j] {
				list[i], list[j] = list[j], list[i]
			}
		}
	}
	return list
}
