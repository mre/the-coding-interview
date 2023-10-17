let resultSequence resultList =
    let folder result state =
        match state, result with
        | Error _, _ -> state
        | Ok listSoFar, Ok value -> Ok(value :: listSoFar)
        | Ok _, Error e -> Error e

    List.foldBack folder resultList (Ok [])

type BracketVariant =
    | Round
    | Square
    | Curly

type BracketDirection =
    | Open
    | Close

type Bracket =
    { variant: BracketVariant
      direction: BracketDirection }

let bracketVariant =
    function
    | '('
    | ')' -> Some Round
    | '['
    | ']' -> Some Square
    | '{'
    | '}' -> Some Curly
    | _ -> None

let bracketDirection =
    function
    | '('
    | '['
    | '{' -> Some Open
    | ')'
    | ']'
    | '}' -> Some Close
    | _ -> None

let bracket char =
    match bracketVariant char, bracketDirection char with
    | Some v, Some d -> Ok { variant = v; direction = d }
    | _ -> Error <| sprintf "Unknown character %c" char

let readString (str: string) =
    str.ToCharArray() |> List.ofArray |> List.map bracket |> resultSequence

let checkBalance brackets =
    let folder state bracket =
        match state, bracket.direction, bracket.variant with
        | None, _, _ -> None
        | Some bracketStack, Open, v -> Some <| v :: bracketStack
        | Some(top :: rest), Close, variant when top = variant -> Some rest
        | Some _, Close, _ -> None

    List.fold folder (Some []) brackets
    |> Option.bind (function
        | [] -> Some []
        | _ -> None) // Expect the stack to be empty at the end
    |> Option.isSome

let balancedBrackets string =
    match readString string with
    | Error error -> Error error
    | Ok brackets -> Ok(checkBalance brackets)

let main () =
    printfn ""
    printfn "Enter a string to check for balance:"
    let string = System.Console.ReadLine()

    match balancedBrackets string with
    | Error e ->
        eprintfn "%s" e
        65
    | Ok true ->
        printfn "The brackets are balanced."
        0
    | Ok false ->
        printfn "The brackets are not balanced."
        0

while true do
    main () |> ignore
