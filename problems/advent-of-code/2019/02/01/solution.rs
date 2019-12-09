use std::env::args;

fn apply<F>(data: &mut Vec<usize>, i: usize, op: F) where F : Fn(usize, usize) -> usize {
    let x = data[i + 3];
    data[x] = op(data[data[i + 1]], data[data[i + 2]]);
}

fn main() {
    let mut data: Vec<usize> = args().nth(1).unwrap().split(",").map(|s| s.parse().unwrap()).collect();
    let mut i: usize = 0;
    while data[i] != 99 {
        match data[i] {
            1 => apply(&mut data, i, |lhs, rhs| lhs + rhs),
            2 => apply(&mut data, i, |lhs, rhs| lhs * rhs),
            _ => panic!("Unknown opcode {}: something went wrong", data[i]),
        }
        i += 4;
    }
    println!("{}", data.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(","));
}
