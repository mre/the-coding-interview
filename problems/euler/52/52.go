package main

import (
	"fmt"
	"reflect"
	"strconv"
	"strings"
)

// GOLANG Y U NO HAVE SETS?!
func intset(x int) map[string]int {
	s := strconv.Itoa(x)
	ss := strings.Split(s, "")
	smap := map[string]int{}

	for i := 0; i < len(ss); i++ {
		(smap[ss[i]])++

	}
	return smap
}

func permutedMutables(x int) bool {
	xSet := intset(x)
	for i := 2; i <= 6; i++ {
		curr := i * x
		currSet := intset(curr)
		if !reflect.DeepEqual(currSet, xSet) {
			return false
		}
	}
	return true
}

func main() {
	i := 2
	for {
		if permutedMutables(i) {
			fmt.Println(i)
			break
		}
		i++
	}
}
