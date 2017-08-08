package main

import "fmt"

func main() {
	fmt.Println(pairs_lin(10, []int{3, 4, 5, 6, 7})) // [[6, 4], [7, 3]]
	fmt.Println(pairs_lin(8, []int{3, 4, 5, 4, 4}))  // [[3, 5], [4, 4], [4, 4], [4, 4]]
	fmt.Println(pairs_lin(8, []int{4}))              // []
	fmt.Println(pairs_lin(0, []int{4, -4}))          // [[-4,4]]
}

func isInSlice(partner int, slice []int) bool {
	for _, c := range slice {
		if partner == c {
			return true
		}
	}
	return false
}

func pairs_lin(k int, arr []int) [][]int {
	var pairs [][]int
	var seen []int
	if len(arr) < 2 {
		return pairs
	}
	var partner int
	for _, n := range arr {
		partner = k - n

		if isInSlice(partner, seen) {
			pairs = append(pairs, []int{n, partner})
		} else {
			seen = append(seen, n)
		}
	}
	return pairs
}
