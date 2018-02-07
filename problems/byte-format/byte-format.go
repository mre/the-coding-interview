package main

import (
	"fmt"
)

func main() {
	fmt.Println(byte_format(156833213, 2))
	fmt.Println(byte_format(8101, 2))
	fmt.Println(byte_format(12331, 3))
}

func byte_format(nbytes float32, round int) string{
	suffixes := []string{"B", "KB", "MB", "GB", "TB", "PB"}
	actSuffix := 0
	
	for{
		if nbytes < 1024{
			break
		}
		
		nbytes = float32(nbytes) / 1024.0
		actSuffix += 1
	}
	
	roundFmt := fmt.Sprintf("%%.%df", round)
	resFmt := fmt.Sprintf("%s %%s", roundFmt)
	res := fmt.Sprintf(resFmt, nbytes, suffixes[actSuffix])
	return res
}