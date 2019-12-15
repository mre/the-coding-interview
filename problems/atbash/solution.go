package main

import (
    "fmt"
    "os"
)

func main() {
    for _, c := range os.Args[1] {
        if c == '\n' {
            fmt.Println()
        } else {
            fmt.Printf("%c", 'z'-(c-'a'))
        }
    }
}
