fn str_split<T: Into<String>>(string: T, delim: char) -> Vec<String> {
    let mut words = vec![];
    let mut curr = String::new();

    for c in string.into().chars() {
        match c == delim {
            true => {
                words.push(curr);
                curr = String::new();
            },
            false => curr.push(c),
        }
    }
    words.push(curr);
    words
}

fn main() {
    println!("{:?}", str_split("hello, world", ','));
}

