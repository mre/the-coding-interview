use std::env::args;

fn apply<F>(data: &mut Vec<usize>, ip: usize, op: F) where F : Fn(usize, usize) -> usize {
    let x = data[ip + 3];
    data[x] = op(data[data[ip + 1]], data[data[ip + 2]]);
}

fn main() {
    let mut data: Vec<usize> = args().nth(1).unwrap().split(",").map(|s| s.parse().unwrap()).collect();
    let mut ip: usize = 0;
    while data[ip] != 99 {
        match data[ip] {
            1 => apply(&mut data, ip, |lhs, rhs| lhs + rhs),
            2 => apply(&mut data, ip, |lhs, rhs| lhs * rhs),
            _ => panic!("Unknown opcode {}", data[ip]),
        }
        ip += 4;
    }
    println!("{}", data.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(","));
}
