use std::collections::HashSet;

fn remove_duplicates(s: &str) -> String  {
  let mut seen: HashSet<String> = HashSet::new();
  let mut new = String::new();

  for char in s.chars() {
    if !seen.contains(&char.to_lowercase().to_string()) {
      new.push(char);
      seen.insert(char.to_lowercase().to_string());
    }
  }
  new
}

fn main() {
  println!("{}", remove_duplicates("tree traversal"));
}


mod tests {
  use super::remove_duplicates;

  #[test]
  fn removes_duplicates_lower() {
    assert_eq!("tre avsl", remove_duplicates("tree traversal"));
  }

  #[test]
  fn removes_duplicates_higher() {
    assert_eq!("TRE AVSL", remove_duplicates("TREE TRAVERSAL"));
  }

  #[test]
  fn removes_duplicates_digits() {
    assert_eq!("2134567", remove_duplicates("212345667"));
  }

  #[test]
  fn removes_duplicates_mixed() {
    assert_eq!("Tr3 4vsl", remove_duplicates("Tr33 tr4v3rs4l"));
  }
}
