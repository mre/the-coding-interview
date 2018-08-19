use std::collections::HashMap;

const CASH_UNITS: [u128; 15] = [
    500_00, 200_00, 100_00, 50_00, 20_00, 10_00, 5_00, 2_00, 1_00, 50, 20, 10, 5, 2, 1,
];

fn cash_units(amount: u128) -> HashMap<u128, u128> {
    let mut rest = amount;
    let mut result = HashMap::new();

    for cash_unit in &CASH_UNITS {
        let n = rest / cash_unit;
        result.insert(*cash_unit, n);
        rest %= cash_unit;
    }

    result
}

fn main() {
    let result = cash_units(197_278);
    assert_eq!(3, result[&500_00]);
    assert_eq!(2, result[&200_00]);
    assert_eq!(0, result[&100_00]);
    assert_eq!(1, result[&50_00]);
    assert_eq!(1, result[&20_00]);
    assert_eq!(0, result[&10_00]);
    assert_eq!(0, result[&5_00]);
    assert_eq!(1, result[&2_00]);
    assert_eq!(0, result[&1_00]);
    assert_eq!(1, result[&50]);
    assert_eq!(1, result[&20]);
    assert_eq!(0, result[&10]);
    assert_eq!(1, result[&5]);
    assert_eq!(1, result[&2]);
    assert_eq!(1, result[&1]);
}
