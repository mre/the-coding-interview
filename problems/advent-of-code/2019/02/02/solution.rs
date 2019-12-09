use std::env::args;
use std::process::exit;

fn apply<F>(data: &mut Vec<usize>, i: usize, op: F) where F : Fn(usize, usize) -> usize {
    let x = data[i + 3];
    data[x] = op(data[data[i + 1]], data[data[i + 2]]);
}

fn int_computer(mut data: Vec<usize>) -> usize {
    let mut i: usize = 0;
    while data[i] != 99 {
        match data[i] {
            1 => apply(&mut data, i, |lhs, rhs| lhs + rhs),
            2 => apply(&mut data, i, |lhs, rhs| lhs * rhs),
            _ => panic!("Unknown opcode {}: something went wrong", data[i]),
        }
        i += 4;
    }
    data[0]
}

fn main() {
    let input: Vec<usize> = args().nth(1).unwrap().split(",").map(|s| s.parse().unwrap()).collect();
    for noun in 0..99 {
        for verb in 0..99 {
            let mut data = input.to_vec();
            data[1] = noun;
            data[2] = verb;
            if int_computer(data) == 19690720 {
                println!("{}", 100 * noun + verb);
                exit(0);
            }
        }
    }
    exit(1);
}
