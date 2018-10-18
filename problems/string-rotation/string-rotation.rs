fn is_rotation(forward: &str, reverse: &str) -> bool {
    let forward_chars: Vec<char> = forward.chars().collect();
    let reverse_chars: Vec<char> = reverse.chars().collect();
    let mut rev_match = true;

    if forward_chars.len() == reverse_chars.len() {
        let mut i = forward_chars.len() - 1;

        for c in forward_chars {
            if c != reverse_chars[i] {
                rev_match = false;
                break;
            }

            i = if i > 0 {
                i - 1
            } else {
                break;
            };
        }
    }

    rev_match
}

fn is_rotation2(forward: &str, reverse: &str) -> bool {
    (forward.len() == reverse.len()) && (forward == reverse.chars().rev().collect::<String>())
}

fn main() {
    println!("{}", is_rotation("ABCD", "DCBA"));
    println!("{}", is_rotation("ABCD", "BCDA"));

    println!("{}", is_rotation2("DACB", "BCAD"));
    println!("{}", is_rotation2("ABCD", "BCDA"));
}
