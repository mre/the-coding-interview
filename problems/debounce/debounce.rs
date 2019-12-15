use std::time::{Duration, Instant};

fn debounce<F: FnMut()>(mut f: F, timeout: u64, pass: bool) -> impl FnMut() {
  let dur = Duration::from_millis(timeout);
  let mut active: Option<Instant> = None;
  move || {
    match active {
      Some(inst) if (inst.elapsed() <= dur) && !pass => {
        active = Some(Instant::now());
      }
      Some(_) | None => {
        f();
        active = Some(Instant::now());
      }
    }
  }
}

fn main() {
  let mut debounced = debounce(|| {println!("debounce!");}, 5, false);
  debounced();
}


mod tests {
  use super::debounce;
  use std::time::Duration;
  use std::thread::sleep;

  #[test]
  fn function_is_called_first_time() {
    let mut start = 0;
    {
      let mut debounced = debounce(|| {
      start += 1;
      }, 10, false);
      debounced();
    }
    assert_eq!(1, start);
  }

  #[test]
  fn function_is_not_called_if_timeout_hasnt_elapsed() {
    let mut start = 0;
    {
      let mut debounced = debounce(|| {
      start += 1;
      }, 100, false);
      debounced();
      debounced();
    }
    assert_eq!(1, start);
  }

  #[test]
  fn function_iscalled_after_timeout_has_elapsed() {
    let mut start = 0;
    let dur = 100;
    {
      let mut debounced = debounce(|| {
      start += 1;
      }, dur, false);
      debounced();
      sleep(Duration::from_millis(dur));
      debounced();
    }
    assert_eq!(2, start);
  }

  #[test]
  fn timeout_is_restarted_if_function_is_called_before_timeout_has_elapsed() {
    let mut start = 0;
    let dur = 100;
    {
      let mut debounced = debounce(|| {
      start += 1;
      }, dur, false);
      debounced();
      sleep(Duration::from_millis(dur - 20));
      debounced();
      sleep(Duration::from_millis(20));
      debounced();
    }
    assert_eq!(1, start);
  }

  #[test]
  fn function_is_called_after_timeout_is_restarted() {
    let mut start = 0;
    let dur = 100;
    {
      let mut debounced = debounce(|| {
      start += 1;
      }, dur, false);
      debounced();
      sleep(Duration::from_millis(dur - 20));
      debounced();
      sleep(Duration::from_millis(20));
      debounced();
      sleep(Duration::from_millis(dur));
      debounced();
    }
    assert_eq!(2, start);
  }

  #[test]
  fn function_is_called_is_pass() {
    let mut start = 0;
    let dur = 100;
    {
      let mut debounced = debounce(|| {
      start += 1;
      }, dur, true);
      debounced();
      debounced();
      debounced();
    }
    assert_eq!(3, start);
  }
}
