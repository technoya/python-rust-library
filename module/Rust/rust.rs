pub extern "C" fn count_up_to(n: u64) -> u64 {
    let mut count = 0;
    for _i in 1..=n {
        count += 1;
    }
    count
}
