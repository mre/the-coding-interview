use std::string::ToString;

fn get_loops(c: char) -> u32 {
    match c {
      '0' | '6' | '9' => 1,
      '8' => 2,
      _ => 0,
    }
}

fn closed_loops<T>(n: T) -> u32 where T: ToString {
  n.to_string().chars().map(get_loops).sum()
}

fn main() {
  assert_eq!(closed_loops(16780), 4);
}
