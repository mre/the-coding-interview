package main

import "fmt"

func main() {
	fmt.Println(anagram("AdnBndAndBdaBn", "dAn")) // 4 ("Adn", "ndA", "dAn", "And")
	fmt.Println(anagram("AbrAcadAbRa", "cAda"))   // 2
}

func is_anagram(token, child string) bool {
	hits := 0
	for _, t := range token {
		for i, c := range child {
			if c == t {
				child = child[:i] + child[i+1:]
				hits++
				break
			}
		}
	}
	return hits == len(token)
}

func anagram(parent, child string) int {
	count := 0
	var end int
	var token string
	for start := 0; start < (len(parent) - len(child)); start++ {
		end = start + len(child)
		token = parent[start:end]
		if is_anagram(token, child) {
			count++
		}
	}
	return count
}
