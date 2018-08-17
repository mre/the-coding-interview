use Either::*;

enum Either<'a> {
    List(&'a [Either<'a>]),
    Int(u32),
}

fn array_sum(input: &[Either]) -> u32 {
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
        array_sum(&[Int(1), Int(2), List(&[Int(3), Int(4), List(&[Int(5)]),]),])
    );
}
