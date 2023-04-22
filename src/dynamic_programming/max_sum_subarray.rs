/*
---
difficulty:
    site: medium
    perceived: hard
url: https://leetcode.com/problems/maximum-subarray
time_complexity: O(n)
space_complexity: O(1)
categories: [dp, sliding_window]
resources:
    - https://www.youtube.com/watch?v=5WZl3MMT0Eg
---
*/

use std::cmp::max;

pub fn max_sub_array(nums: Vec<i32>) -> i32 {
    let mut sum = nums[0];
    let mut max_sum = sum;

    for num in &nums[1..] {
        sum = max(*num, sum+num);
        max_sum = max(max_sum, sum);
    }
    max_sum
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let nums = vec![1];

        let actual = max_sub_array(nums);

        assert_eq!(actual, 1);
    }

    #[test]
    fn test_2() {
        let nums = vec![-1];

        let actual = max_sub_array(nums);

        assert_eq!(actual, -1);
    }

    #[test]
    fn test_3() {
        let nums = vec![5, 4, -1, 7, 8];

        let actual = max_sub_array(nums);

        assert_eq!(actual, 23);
    }

    #[test]
    fn test_4() {
        let nums = vec![-2, 1, -3, 4, -1, 2, 1, -5, 4];

        let actual = max_sub_array(nums);

        assert_eq!(actual, 6);
    }

    #[test]
    fn test_5() {
        let nums = vec![-2, -1];

        let actual = max_sub_array(nums);

        assert_eq!(actual, -1);
    }
}
