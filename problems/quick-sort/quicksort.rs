use std::fmt::Debug;

#[allow(dead_code)]
fn quicksort<T: Ord>(arr: &mut [T]) {
    let length = arr.len();
    if length < 2 {
        return;
    }

    let (mut pivot, mut end) = (0, length - 1);
    for _ in 0..length - 1 {
        if arr[pivot] < arr[pivot + 1] {
            arr.swap(pivot + 1, end);
            end -= 1;
        } else {
            arr.swap(pivot, pivot + 1);
            pivot += 1;
        }
    }
    quicksort(&mut arr[..pivot]);
    quicksort(&mut arr[pivot + 1..]);
}

pub fn is_sorted<T: Ord + Debug>(arr: &[T]) ->  bool {
    // This output will be supressed by default
    // Run to see it.
    println!("{:?}", arr);
    for win in arr.windows(2) {
        if win[0] > win[1] {
            return false;
        }
    }
    return true;
}

fn get_test_vecs() -> Vec<Vec<u64>> {
    vec![vec![],
         vec![1],
         vec![1, 2],
         vec![2, 1],
         vec![1, 2, 3],
         vec![2, 1, 3],
         vec![3, 1, 2],
         vec![8, 5, 2, 6, 9, 3],
         vec![2, 3, 5, 6, 8, 9],
         vec![9, 8, 6, 5, 3, 2],
         vec![8, 4, 7, 3, 6, 2, 5, 1],
         vec![8, 1, 7, 2, 6, 3, 5, 4],
         vec![8, 1, 7, 2, 6, 3, 5, 4],
         vec![16, 14, 1, 1, 7, 18, 7, 6, 8, 18, 5],
         vec![19, 18, 14, 15, 3, 9, 8, 2, 2, 20, 11],
         vec![2, 3, 8, 7, 23, 26, 19, 29, 23, 32, 20, 18, 11, 11, 24, 13, 17],
         vec![0, 3, 7, 6],
         vec![6, 4, 4, 5, 11, 10, 10],
         vec![15, 13, 17, 1, 1, 19, 3, 19, 0, 11],
         vec![19, 19, 21, 21, 22, 25, 19, 14, 23, 25, 14, 10, 8, 4, 28, 12, 2, 33],
         vec![8, 1, 0, 5, 3],
         vec![27, 14, 22, 10, 8, 23, 7, 32, 28, 31, 9, 19, 30, 28, 21, 20, 13],
         vec![2, 1, 4, 17, 5, 17, 8, 2, 13, 13]]
}

fn main() {
    let mut tests = get_test_vecs();

    for test in tests.iter_mut() {
        let input = test.as_mut();
        //let result = vec![1, 2, 3];
        quicksort(input);
        assert!(is_sorted(input));
    }
}
