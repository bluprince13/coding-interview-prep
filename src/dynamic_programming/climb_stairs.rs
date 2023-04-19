// https://leetcode.com/problems/climbing-stairs

// +-------+---------------+--------+
// | steps |    sequence   |  total |
// +-------+---------------+--------+
// |     1 | 1             |      1 |
// |     2 | 1 + 1         |      2 |
// |       | 2             |        |
// |     3 | 1 + 1 + 1     |      3 |
// |       | 1 + 2         |        |
// |       | 2 + 1         |        |
// |     4 | 1 + 1 + 1 + 1 |      5 |
// |       | 1 + 2 + 1     |        |
// |       | 2 + 1 + 1     |        |
// |       | 1 + 1 + 2     |        |
// |       | 2 + 2         |        |
// +-------+---------------+--------+

// To get to the 3rd step, you can either
//  take 2 steps from the 1st step
//  take 1 step from the 2nd step
// To get to the 4th step, you can either
//  take 2 steps from the 2nd step
//  take 1 step from the 3rd step

pub fn climb_stairs(n: i32) -> i32 {
    let mut cache = [1, 2];
    if let Some(result) = cache.get((n - 1) as usize) {
        return *result;
    }
    for _ in 3..(n + 1) {
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
        let actual = climb_stairs(1);

        assert_eq!(actual, 1);
    }

    #[test]
    fn test_2() {
        let actual = climb_stairs(2);

        assert_eq!(actual, 2);
    }

    #[test]
    fn test_3() {
        let actual = climb_stairs(3);

        assert_eq!(actual, 3);
    }
}
