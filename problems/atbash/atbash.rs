fn atbash(input: String) -> String {
    let search = "abcdefghijklmnopqrstuvwxyz";
    let replace: String = search.chars().rev().collect();
    input.chars().map(|c| replace.chars().nth(search.find(c).unwrap()).unwrap()).collect()
}

fn main() {
    println!("{:?}", atbash("hello".to_string()));
    println!("{:?}", atbash("test".to_string()));
    println!("{:?}", atbash("wizard".to_string()));
    println!("{:?}", atbash("glow".to_string()));
}
