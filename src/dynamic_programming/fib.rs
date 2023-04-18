// https://leetcode.com/problems/fibonacci-number/?envType=study-plan&id=dynamic-programming-i

pub fn fib(n: i32) -> i32 {
    let mut cache = [0, 1];
    if let Some(result) = cache.get(n as usize) {
        return *result;
    }
    for _ in 2..(n + 1) {
        let next = cache.iter().sum();
        cache.rotate_left(1);
        cache[1] = next;
    }
    cache[1]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let actual = fib(0);

        assert_eq!(actual, 0);
    }

    #[test]
    fn test_2() {
        let actual = fib(1);

        assert_eq!(actual, 1);
    }

    #[test]
    fn test_3() {
        let actual = fib(3);

        assert_eq!(actual, 2);
    }
}
