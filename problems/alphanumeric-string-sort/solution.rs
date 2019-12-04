use std::iter::FromIterator;

fn main() {
    let mut parts: [Vec<char>; 4] = Default::default();
    for c in ::std::env::args().nth(1).unwrap().chars() {
        match c {
            'a'..='z' => parts[0].push(c),
            'A'..='Z' => parts[1].push(c),
            '0' | '2' | '4' | '6' | '8' => parts[2].push(c),
            _ => parts[3].push(c),
        }
    }
    let mut result = String::new();
    for part in parts.iter_mut() {
        part.sort();
        result.push_str(&String::from_iter(&*part));
    }
    println!("{}", result)
}
