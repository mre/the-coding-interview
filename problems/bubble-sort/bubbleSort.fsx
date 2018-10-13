let swap i j (arr : 'a array) =
    let temp = arr.[i]
    arr.[i] <- arr.[j]
    arr.[j] <- temp

let bubbleSort (arr : 'a array) =
    let rec sort (arr : 'a array) =
        let mutable swapCount = 0
        for i = 0 to arr.Length - 2 do
            if arr.[i] > arr.[i + 1] then
                swap i (i + 1) arr
                swapCount <- swapCount + 1

        if swapCount > 0 
        then sort arr 
        else arr
    sort arr

// Test
// prints: -10 0 1 2 3 4 5 50 100
[|5;3;1;2;4;100;0;50;-10|] |> bubbleSort |> Array.iter (printf "%i ")