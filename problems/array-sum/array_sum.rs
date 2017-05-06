// Solution discussed here:
// https://users.rust-lang.org/t/an-idiomatic-way-to-sum-up-values-in-a-multidimensional-array/9485
fn main() {
    println!("{}", sum(vec![vec![1, 2], vec![3], vec![4, 5, 6]]));
}
fn sum<T, U, V>(i: U) -> T
    where T: Sum,
          U: IntoIterator<Item = V>,
          V: IntoIterator<Item = T>
{
    i.into_iter().flat_map(IntoIterator::into_iter).sum()
}
