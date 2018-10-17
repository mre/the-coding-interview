fn diff(num: i32, integers: Vec<i32>) -> i32 {
    let mut count = 0;

    for (i, int_elem1) in integers.iter().enumerate() {
        for (j, int_elem2) in integers.iter().enumerate() {
            let index_diff: i32 = if (i - j) > 0 { (i - j) as i32 } else { 0 };
            if index_diff == num && int_elem1 != int_elem2 {
                count = count + 1;
            }
        }
    }

    return (count / 2) - (count % 2);
}

fn main() {
    println!("{}", diff(4, vec![1, 1, 5, 6, 9, 16, 27]));
    println!("{}", diff(2, vec![1, 1, 3, 3]));
}
