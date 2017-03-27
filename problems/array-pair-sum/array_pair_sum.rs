use std::collections::HashSet;
type Pair = (i64, i64);

fn array_pair_sum(values: Vec<i64>, k: i64) -> HashSet<Pair> {
    let mut pairs: HashSet<Pair> = HashSet::new();
    let mut seen: HashSet<i64> = HashSet::new();

    for v1 in &values {
        let other = k - v1;
        if seen.contains(&other) {
            pairs.insert((*v1, other));
        }
        seen.insert(*v1);
    }
    pairs
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_array_pair_sum() {
        let mut expected1: HashSet<Pair> = HashSet::new();
        expected1.insert((6, 4));
        expected1.insert((7, 3));
        assert_eq!(array_pair_sum(vec![3, 4, 5, 6, 7], 10), expected1);

        let mut expected2: HashSet<Pair> = HashSet::new();
        expected2.insert((5, 3));
        expected2.insert((4, 4));
        assert_eq!(array_pair_sum(vec![3, 4, 5, 4, 4], 8), expected2);

        assert!(array_pair_sum(vec![4], 8).is_empty());

        let mut expected3: HashSet<Pair> = HashSet::new();
        expected3.insert((-4, 4));
        assert_eq!(array_pair_sum(vec![4, -4], 0), expected3);
    }
}

