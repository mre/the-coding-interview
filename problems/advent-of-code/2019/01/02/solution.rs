use std::cmp::max;

fn main() {
    let mut sum: i32 = 0;
    for line in ::std::env::args().nth(1).unwrap().lines() {
        let mut x = line.parse::<i32>().unwrap();
        while x > 0 {
            x = max(0, x / 3 - 2);
            sum += x;
        }
    }
    println!("{}", sum);
}
