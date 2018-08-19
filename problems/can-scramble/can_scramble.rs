trait CharSum {
    fn char_sum(self) -> u128;
}

impl<'a> CharSum for &'a str {
    fn char_sum(self) -> u128 {
        self.bytes().map(|it| it as u128).sum()
    }
}

fn can_scramble(input: &str, output: &str) -> bool {
    input.len() == output.len() && input.char_sum() == output.char_sum()
}

fn main() {
    assert!(can_scramble("abc", "cab"));
    assert!(!can_scramble("aab", "bba"));
}
