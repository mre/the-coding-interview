use std::collections::HashMap;

// Split up a given string slice into all possible substrings of length n.
// Adapted from http://stackoverflow.com/a/30890221
fn offset_slices(s: &str, n: usize) -> Vec<&str> {
    if s.len() < n {
        return vec![s];
    }
    (0..s.len() - n + 1).map(|i| &s[i..i + n]).collect()
}

// Create a custom trait for hashing our data
trait Hash {
    fn hash(&self) -> u64;
}

// Hashing a character means mapping it to a prime number
impl Hash for char {
    fn hash(&self) -> u64 {
        match *self {
            'a' => 2,
            'b' => 3,
            'c' => 5,
            'd' => 7,
            'e' => 11,
            'f' => 13,
            'g' => 17,
            'h' => 19,
            'i' => 23,
            'j' => 29,
            'k' => 31,
            'l' => 37,
            'm' => 41,
            'n' => 43,
            'o' => 47,
            'p' => 53,
            'q' => 59,
            'r' => 61,
            's' => 67,
            't' => 71,
            'u' => 73,
            'v' => 79,
            'w' => 83,
            'x' => 89,
            'y' => 97,
            'z' => 101,
            'A' => 103,
            'B' => 107,
            'C' => 109,
            'D' => 113,
            'E' => 127,
            'F' => 131,
            'G' => 137,
            'H' => 139,
            'I' => 149,
            'J' => 151,
            'K' => 163,
            'L' => 167,
            'M' => 173,
            'N' => 179,
            'O' => 181,
            'P' => 191,
            'Q' => 193,
            'R' => 197,
            'S' => 199,
            'T' => 211,
            'U' => 223,
            'V' => 227,
            'W' => 229,
            'X' => 233,
            'Y' => 239,
            'Z' => 241,
            _ => panic!("ASCII only"),
        }
    }
}

// The hash of a String is the product of all character hashes
impl Hash for String {
    fn hash(&self) -> u64 {
        self.chars().fold(1, |mult, c| mult * c.hash())
    }
}

fn anagram_detection(parent: &str, child: &str) -> usize {
    let mut matches: Vec<String> = Vec::new();
    let child_hash = String::from(child).hash();

    for slice in offset_slices(parent, child.len()) {
        if String::from(slice).hash() == child_hash {
            matches.push(slice.into())
        }
    }

    return matches.len();
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_offset_slices() {
        assert_eq!(offset_slices("helloworld", 100), vec!["helloworld"]);
        assert_eq!(offset_slices("helloworld", 3),
                   vec!["hel", "ell", "llo", "low", "owo", "wor", "orl", "rld"]);
        assert_eq!(offset_slices("helloworld", 10), vec!["helloworld"]);
        assert_eq!(offset_slices("helloworld", 9),
                   vec!["helloworl", "elloworld"]);
    }

    #[test]
    fn test_anagram_detection() {
        assert_eq!(anagram_detection("AdnBndAndBdaBn", "dAn"), 4);
        assert_eq!(anagram_detection("AbrAcadAbRa", "cAda"), 2);
    }
}

