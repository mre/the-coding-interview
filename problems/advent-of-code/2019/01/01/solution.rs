fn main() {
    println!(
        "{}",
        ::std::env::args()
            .nth(1).unwrap()
            .lines()
            .map(|x| x.parse::<i32>().unwrap() / 3 - 2)
            .sum::<i32>()
    );
}
