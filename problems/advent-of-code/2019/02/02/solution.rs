use std::env::args;
use std::process::exit;

fn apply<F>(data: &mut Vec<usize>, ip: usize, op: F) where F : Fn(usize, usize) -> usize {
    let x = data[ip + 3];
    data[x] = op(data[data[ip + 1]], data[data[ip + 2]]);
}

fn int_computer(mut data: Vec<usize>) -> usize {
    let mut ip: usize = 0;
    while data[ip] != 99 {
        match data[ip] {
            1 => apply(&mut data, ip, |lhs, rhs| lhs + rhs),
            2 => apply(&mut data, ip, |lhs, rhs| lhs * rhs),
            _ => panic!("Unknown opcode {}", data[ip]),
        }
        ip += 4;
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
