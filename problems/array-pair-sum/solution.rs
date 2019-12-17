use std::cmp::{max, min};
use std::collections::HashSet;
use std::fmt::{Display, Formatter, Result};

struct Pair(i32, i32);

impl Display for Pair {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "({}, {})", self.0, self.1)
    }
}

fn main() {
    let input: Vec<i32> = ::std::env::args()
        .nth(1)
        .unwrap()
        .split(",")
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
    let k = input[0];
    let mut seen: HashSet<i32> = HashSet::new();
    let mut pairs: Vec<Pair> = vec![];

    for n in input.iter().skip(1) {
        let x = k - n;
        if x != *n {
            if seen.contains(&x) {
                pairs.push(Pair(min(x, *n), max(x, *n)));
            } else {
                seen.insert(*n);
            }
        }
    }

    print!("[");
    for (i, pair) in pairs.iter().enumerate() {
        if i != 0 {
            print!(", ");
        }
        print!("{}", pair);
    }
    print!("]");
}
