//returns the missing number, or in the case Vec is empty, returns None
fn missing_number(input: &[usize]) -> Option<usize> {
    if input.is_empty() {
        return None;
    }

    let non_missing: usize = (1..input.len() + 2).sum();
    let missing: usize = input.iter().sum();

    Some(non_missing - missing)
}

fn main() {
    println!(
        "missing number: {}",
        missing_number(&[1, 2, 3, 4, 6]).unwrap()
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn returns_none_if_vec_is_empty() {
        assert_eq!(None, missing_number(&[]));
    }

    #[test]
    fn finds_missing_number_sequential_range() {
        assert_eq!(4, missing_number(&[1, 2, 3, 5, 6]).unwrap());
    }
}
