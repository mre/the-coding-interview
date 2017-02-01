fn reverse<T>(s: T) -> String where T: Into<String> {
  s.into().chars().rev().collect()
}

fn main() {
    println!("{}", reverse("hello élle  今日は"));
}
