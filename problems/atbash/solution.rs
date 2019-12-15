fn main() {
    ::std::env::args()
        .nth(1)
        .unwrap()
        .chars()
        .for_each(|c| print!("{}", if c == '\n' { c } else { (b'z' - ((c as u8) - b'a')) as char }))
}
