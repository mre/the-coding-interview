enum Either {
    List(Vec<Either>),
    Int(u32),
}

fn array_sum(input: Vec<Either>) -> u32 {
    if input.is_empty() {
        0
    } else {
        let mut result = 0;
        let mut stack = vec![&input];
        while let Some(next) = stack.pop() {
            for item in next.iter() {
                match item {
                    Either::List(it) => stack.push(it),
                    Either::Int(it) => result += it,
                }
            }
        }
        result
    }
}

fn main() {
    assert_eq!(
        15,
        array_sum(vec![
            Either::Int(1),
            Either::Int(2),
            Either::List(vec![
                Either::Int(3),
                Either::Int(4),
                Either::List(vec![Either::Int(5)]),
            ]),
        ])
    );
}
