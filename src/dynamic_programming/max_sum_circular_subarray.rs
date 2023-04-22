/*
---
difficulty:
    site: medium
    perceived: hard
url: https://leetcode.com/problems/maximum-sum-circular-subarray
space_complexity: O(1)
categories: [dp, sliding_window]
resources:
    - https://www.youtube.com/watch?v=fxT9KjakYPM
---
*/

use std::cmp::{max, min};

pub fn max_subarray_sum_circular(nums: Vec<i32>) -> i32 {
    let mut current_max = nums[0];
    let mut current_min = nums[0];
    let mut global_max = current_max;
    let mut global_min = current_max;
    let mut total_sum = current_max;

    for num in &nums[1..] {
        current_max = max(*num, current_max + num);
        current_min = min(*num, current_min + num);
        total_sum += num;
        global_max = max(global_max, current_max);
        global_min = min(global_min, current_min);
    }

    // For edge case when all numbers are negative, return global_max
    if total_sum == global_min {
        global_max
    } else {
        max(global_max, total_sum - global_min)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let nums = vec![5, -3, 5];

        let actual = max_subarray_sum_circular(nums);

        assert_eq!(actual, 10);
    }

    #[test]
    fn test_2() {
        let nums = vec![-3, -2, -3];

        let actual = max_subarray_sum_circular(nums);

        assert_eq!(actual, -2);
    }
}
