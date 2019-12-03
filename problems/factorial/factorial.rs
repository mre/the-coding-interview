fn iterative(n: u128) -> u128 {
    if n <= 1 { 1 } else {
        let mut acc = 1u128;
        let mut x = n;
        while x > 1 {
            acc *= x;
            x -= 1;
        }
        acc
    }
}

fn recursive(n: u128) -> u128 {
    if n <= 1 { 1 } else { n * recursive(n - 1) }
}

mod tests {
    #[test]
    fn iterative_test() {
        use super::iterative;

        assert_eq!(iterative(0), 1);
        assert_eq!(iterative(1), 1);
        assert_eq!(iterative(2), 2);
        assert_eq!(iterative(3), 6);
        assert_eq!(iterative(4), 24);
        assert_eq!(iterative(5), 120);
        assert_eq!(iterative(20), 2_432_902_008_176_640_000);
    }

    #[test]
    fn recursive_test() {
        use super::recursive;

        assert_eq!(recursive(0), 1);
        assert_eq!(recursive(1), 1);
        assert_eq!(recursive(2), 2);
        assert_eq!(recursive(3), 6);
        assert_eq!(recursive(4), 24);
        assert_eq!(recursive(5), 120);
        assert_eq!(recursive(20), 2_432_902_008_176_640_000);
    }
}
