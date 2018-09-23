package main

import (
	"fmt"
	"math"
)

func factorial(n uint64) float64 {
	return math.Gamma(float64(n) + 1)
}

func combinations(n, r uint64) uint64 {
	denominator := (factorial(r) * factorial(n-r))
	return uint64(factorial(n) / denominator)
}

func main() {
	count := 0
	for n := uint64(23); n <= 100; n++ {
		for r := uint64(1); r <= n; r++ {
			if (combinations(n, r)) > 1000000 {
				count++
			}
		}
	}
	fmt.Println(count)
}
