use std::collections::HashMap;

fn balanced_brackets(s: &str) -> bool {
  // Use a vector as a stack
  let mut stack = Vec::new();

  let mut matches = HashMap::new();
  matches.insert(')', '(');
  matches.insert(']', '[');
  matches.insert('}', '{');

  for c in s.chars() {
    match c {
      '(' | '[' | '{' => stack.push(c),
      ')' | ']' | '}' => {
        let prev = stack.pop();
        match matches.get(&c) {
          Some(prev) => (),
          _ => unreachable!()
        }
      }
      _ => return false, // Not a bracket
    }
  }
  true
}

fn main() {
    assert_eq!(true, balanced_brackets("{([][[[][]({})]])}"));
}
