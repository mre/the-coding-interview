package main

import (
	"fmt"
	"sort"
)

var bytesInOrder map[byte]uint8

func init() {
	bytesInOrder = make(map[byte]uint8)
	orderSlice := []byte("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0246813579")
	for idx, val := range orderSlice {
		bytesInOrder[val] = uint8(idx)
	}
}

// AlphanumericString is a type for alphanumeric string
type AlphanumericString []byte

func (a AlphanumericString) Len() int           { return len(a) }
func (a AlphanumericString) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a AlphanumericString) Less(i, j int) bool { return bytesInOrder[a[i]] < bytesInOrder[a[j]] }

func alphanumSort(str string) string {
	alphanumStr := AlphanumericString([]byte(str))
	sort.Sort(alphanumStr)
	return string(alphanumStr)
}

func main() {
	fmt.Println(alphanumSort("Sorting0123456789"))           // ginortS0246813579
	fmt.Println(alphanumSort("foobar1237348421"))            // abfoor2244811337
	fmt.Println(alphanumSort("789765445whjdbjwhwfbs977865")) // bbdfhhjjswww446688555777799
}
