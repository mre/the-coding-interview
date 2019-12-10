package main

import (
    "fmt"
    "os"
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

type Alnum []byte

func (a Alnum) Len() int {
    return len(a)
}

func (a Alnum) Swap(i, j int) {
    a[i], a[j] = a[j], a[i]
}

func (a Alnum) Less(i, j int) bool {
    return bytesInOrder[a[i]] < bytesInOrder[a[j]]
}

func main() {
    alnum := Alnum([]byte(os.Args[1]))
    sort.Sort(alnum)
    fmt.Println(string(alnum))
}
