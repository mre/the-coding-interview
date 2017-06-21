use std::collections::HashMap;

fn can_scramble(input: &str, output: &str) -> bool {
  let mut input_counter = HashMap::new();
  for c in input.chars() {
    let new_count = match input_counter.get(&c) {
      Some(count) => count +1,
      None => 1
    };
    input_counter.insert(c, new_count);
  }
  for c in output.chars() {
    let new_count = match input_counter.get(&c) {
      Some(count) => count -1,
      None => -1
    };
    if new_count < 0 {
      return false;
    }
    input_counter.insert(c, new_count);
  }
  true
}

fn main() {
  assert_eq!(can_scramble("abc", "cab"), true);
}
