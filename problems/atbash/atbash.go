package main

import (
	"fmt"
	"strings"
)

func main() {
	fmt.Println(atbash("abcdefghijklmnopqrstuvwxyz"))
	fmt.Println(atbash("old"))
	fmt.Println(atbash("LOW"))
	fmt.Println(atbash("?"))
}

func atbash(s string) string{
	s = strings.ToLower(s)
	res := ""
	
	for _,c := range(s){
		var decodedChar rune
		if c < rune('a') || c > rune('z'){
			decodedChar = c
		}else{
			diff := c - 'a'
			decodedChar = 'z' - diff
		}
		res = fmt.Sprintf("%s%c", res, decodedChar)
	}
	return res
}

