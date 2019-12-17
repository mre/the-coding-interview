package main

import (
    "fmt"
    "os"
    "strconv"
    "strings"
)

type Pair struct {
    first int
    second int
}

func Min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func Max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func main() {
    var input []int
    for _, x := range strings.Split(os.Args[1], ",") {
        x, _ := strconv.Atoi(x)
        input = append(input, x)
    }
    //noinspection GoNilness
    k := input[0]
    seen := map[int]bool{}
    var pairs []Pair
    //noinspection GoNilness
    for _, n := range input[1:] {
        x := k - n
        if x != n {
            if seen[x] {
                pairs = append(pairs, Pair{Min(x, n), Max(x, n)})
            } else {
                seen[n] = true
            }
        }
    }
    fmt.Print("[")
    for i, pair := range pairs {
        if i != 0 {
            fmt.Print(", ")
        }
        fmt.Printf("(%d, %d)", pair.first, pair.second)
    }
    fmt.Print("]")
}
