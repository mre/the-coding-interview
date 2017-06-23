use std::cmp::PartialOrd;

/// An in-place implementation of bubble sort
fn bubble_sort<T>(arr: &mut [T])
where T: PartialOrd {
  for i in 0..arr.len() {
    for j in i..arr.len() {
      if arr[i] > arr[j] {
        arr.swap(i, j);
      }
    }
  }
}

fn main() {
  let arr = &mut [5,4,1,2,3];
  bubble_sort(arr);
  assert_eq!(&[1,2,3,4,5], arr);
}
