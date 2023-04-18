// https://leetcode.com/problems/n-th-tribonacci-number/

pub fn tribonacci(n: i32) -> i32 {
    let mut cache = [0, 1, 1];
    if let Some(result) = cache.get(n as usize) {
        return *result;
    }
    for _ in 3..(n + 1) {
        let next = cache.iter().sum();
        cache.rotate_left(1);
        cache[2] = next;
    }
    cache[2]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let actual = tribonacci(0);

        assert_eq!(actual, 0);
    }

    #[test]
    fn test_2() {
        let actual = tribonacci(1);

        assert_eq!(actual, 1);
    }

    #[test]
    fn test_3() {
        let actual = tribonacci(4);

        assert_eq!(actual, 4);
    }
}
