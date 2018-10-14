let isValidInterleave (s1 : string) (s2 : string) (s3 : string) =
    let carr1 = s1.ToCharArray()
    let carr2 = s2.ToCharArray()
    let carr3 = s3.ToCharArray()
    
    carr3 = (carr1 |> Seq.zip carr2 |> Seq.collect (fun (f, s) -> f::[s]) |> Seq.toArray) ||
    carr3 = (carr2 |> Seq.zip carr1 |> Seq.collect (fun (f, s) -> f::[s]) |> Seq.toArray)

// test
let s1 = "abc"
let s2 = "def"
let shouldMatch1 = "adbecf"
let shouldMatch2 = "daebfc"
let shouldNotMatch1 = "defabc"
let shouldNotMatch2 = "abcdef"

let test = isValidInterleave s1 s2

//true, true, false, false
test shouldMatch1
test shouldMatch2
test shouldNotMatch1
test shouldNotMatch2