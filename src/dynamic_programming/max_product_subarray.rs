/*
---
difficulty:
    site: medium
    perceived: medium
url: https://leetcode.com/problems/maximum-product-subarray
time_complexity: O(n)
space_complexity: O(1)
categories: [dp]
resources: []
---
*/

use std::cmp::max;

// zeros are a natural breakpoint
// Even numbers of negative numbers could be part of the subarray
// However, an odd number of negative numbers implies a break point either at
// the leftmost negative number or rightmost negative number

pub fn max_product(nums: Vec<i32>) -> i32 {
    let nums_reverse: Vec<&i32> = nums.iter().rev().collect();
    let mut prefix_product = 0;
    let mut suffix_product = 0;
    let mut max_product = nums[0];
    for i in 0..nums.len() {
        prefix_product = nums[i] * if prefix_product == 0 { 1 } else { prefix_product };
        suffix_product = nums_reverse[i] * if suffix_product == 0 { 1 } else { suffix_product };
        max_product = max(max_product, max(prefix_product, suffix_product));
    }
    max_product
}

#[cfg(test)]

mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let nums = vec![2, 3, -2, 4];

        let actual = max_product(nums);

        assert_eq!(actual, 6);
    }

    #[test]
    fn test_2() {
        let nums = vec![-2, 0, -1];

        let actual = max_product(nums);

        assert_eq!(actual, 0);
    }

    #[test]
    fn test_3() {
        let nums = vec![-2, 3, -4];

        let actual = max_product(nums);

        assert_eq!(actual, 24);
    }

    #[test]
    fn test_4() {
        let nums = vec![2, -5, -2, -4, 3];

        let actual = max_product(nums);

        assert_eq!(actual, 24);
    }
}
