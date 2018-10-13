open System.Numerics

// tail recursive version
let fibonacci (n : int) =
    let rec fibonacci' (n:BigInteger, a:BigInteger, b:BigInteger) =
        match n with
        | n when n = 0I -> a
        | _ -> fibonacci' ((n - 1I), b, (a + b))
    fibonacci' (bigint(n), 0I, 1I)

// test
// prints: 6765
fibonacci 20 |> (printfn "%A")

// prints 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
[1..20] |> List.map fibonacci |> List.iter (printf "%A ")