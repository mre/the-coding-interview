package main

import (
	"fmt"
)

func main() {
	fmt.Println(balanced_brackets("()[]{}(([])){[()][]}"))
	fmt.Println(balanced_brackets("())[]{}"))
	fmt.Println(balanced_brackets("[(])"))
}

func balanced_brackets(s string) bool{
	symbols := map[rune]rune{
		'{':'}',
		'(':')',
		'[':']',
	}
	queue := []rune{}
	queueLen := 0
	
	for _,c := range(s){
		queueLen = len(queue)
		if c == '{' || c == '(' || c == '['{
			// it is start symbol
			queue = append(queue, c)
		}else{
			if queueLen < 1{
				return false
			}
			expectedEndSymbol := symbols[queue[queueLen-1]]
			if c == expectedEndSymbol{
				queue = queue[:queueLen-1]
			}else{
				return false
			}
		}
	}
	return true
}

