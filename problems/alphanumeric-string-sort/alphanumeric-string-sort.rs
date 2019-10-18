use std::iter::FromIterator;

fn sort(string: &str) -> String {
  let mut ords : [Vec<char>; 4] = Default::default();
  for ch in string.chars() {
    match ch {
      'a'..= 'z' => ords[0].push(ch),
      'A'..= 'Z' => ords[1].push(ch),
      '0'..= '9' if ch.to_digit(10).unwrap() % 2 == 0 => ords[2].push(ch),
      '0'..= '9' => ords[3].push(ch),
      _ => println!("{} is not alphanumeric", ch)
    }
  }
  let mut ord_string = String::new();
  for ord in ords.iter_mut() {
    ord.sort();
    ord_string.push_str(&String::from_iter(&*ord));
  }
  ord_string
}

fn main() {
  println!("{}", sort("Sorting0123456789"));// ginortS0246813579
}


mod tests {
  use super::sort;

  #[test]
  fn sorts() {
    assert_eq!("ginortS0246813579", sort("Sorting0123456789"));
  }

  #[test]
  fn sorts_lowercase() {
    assert_eq!("abfoor2244811337", sort("foobar1237348421"));
  }

  #[test]
  fn sorts_numbers() {
    assert_eq!("02466881355799", sort("90856123456789"));
  }

}
