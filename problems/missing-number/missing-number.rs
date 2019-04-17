//returns the missing number, or in the case Vec is empty, returns None
fn missing_number(input: &[isize]) -> isize {
    let non_missing: usize = (1..input.len() + 2).sum();
    let missing: isize = input.iter().sum();
    non_missing as isize - missing
}

fn main() {
    println!("missing number: {}", missing_number(&[1, 2, 3, 4, 6]));
}
