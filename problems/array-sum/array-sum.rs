use Either::*;

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
                    List(it) => stack.push(it),
                    Int(it) => result += it,
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
            Int(1),
            Int(2),
            List(vec![Int(3), Int(4), List(vec![Int(5)]),]),
        ])
    );
}
