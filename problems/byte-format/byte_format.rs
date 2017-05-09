const UNITS: [&'static str; 6] = ["B", "KB", "MB", "GB", "TB", "PB"];

fn byte_format(n: usize) -> String {
    let mut id = 0;
    let factor = 1024.0;
    let mut n = n as f64;
    while n > factor {
        n = n / factor;
        id += 1
    }
    format!("{:.2} {}",n, UNITS[id])
}

fn main() {
assert_eq!(byte_format(156833213), "149.57 MB".to_owned());
assert_eq!(byte_format(8101), "7.91 KB".to_owned());
assert_eq!(byte_format(12331), "12.04 KB".to_owned());
}
