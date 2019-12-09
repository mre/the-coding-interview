fn main() {
    let input = ::std::env::args().nth(1).unwrap();
    let mut lines = input.split('\n');

    let parent = lines.nth(0).unwrap();
    let parent_len = parent.len();

    let child = lines.nth(0).unwrap();
    let child_len = child.len();


    if parent_len == child_len {
        println!("{}", if sum(parent) == sum(child) { 1 } else { 0 })
    } else {
        let child_sum = sum(child);
        let mut result = 0usize;
        let mut start = 0usize;
        let mut end = child_len;

        while end < parent_len {
            if sum(&parent[start..end]) == child_sum { result += 1; }
            start += 1;
            end += 1;
        }

        println!("{}", result);
    }
}

fn sum(data: &str) -> usize {
    data.chars().fold(0, |acc, c| acc + (c as usize))
}
