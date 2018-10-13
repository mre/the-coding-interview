// Simple recursive solution with pattern matching.
let factorial n =
    let rec factorial' n acc =
        match n with
        | 0 -> acc
        | _ -> factorial' (n - 1) (acc * n)
    factorial' n 1

// Another solution using List.fold
let factorial2 n = 
    [1..n] |> List.fold (*) 1

// test
// prints: 120
printfn "%i" (factorial 5)
printfn "%i" (factorial2 5)

// prints: 1 1 2 6 24 120 720 5040 40320 362880 3628800
[0..10] |> List.map factorial |> List.iter (printf "%i ")
[0..10] |> List.map factorial2 |> List.iter (printf "%i ")