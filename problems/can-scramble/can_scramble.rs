use std::collections::HashMap;

trait CharMap {
    fn char_map(self) -> HashMap<char, u32>;
}

impl<'a> CharMap for &'a str {
    fn char_map(self) -> HashMap<char, u32> {
        let mut map = HashMap::new();
        for c in self.chars() {
            map.entry(c).and_modify(|count| *count += 1).or_insert(1);
        }
        map
    }
}

pub fn can_scramble(input: &str, output: &str) -> bool {
    input.char_map() == output.char_map()
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn it_works() {
        assert_eq!(can_scramble("", ""), true);
        assert_eq!(can_scramble("abc", "cba"), true);
        assert_eq!(can_scramble("aaa", "aa"), false);
        assert_eq!(can_scramble("aab", "bba"), false);
        assert_eq!(can_scramble("ac", "bb"), false);
    }
}
