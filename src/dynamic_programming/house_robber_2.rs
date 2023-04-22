/*
---
difficulty:
    site: medium
    perceived: medium
url: https://leetcode.com/problems/house-robber-ii
time_complexity: O(n);
space_complexity: 1;
categories: [dp]
---
*/

use std::cmp::max;

// Amount from house i is max(amount from house i-2 + amount from house i,
// amount from house i-1)
// Example: [1, 2, 3, 4, 5]
// If house 1 is included, then house 5 cannot be included
// If house 1 is not included, then house 5 may or may not be included
// We need to find the max of these two possibilities

pub fn rob(nums: Vec<i32>) -> i32 {
    fn solve(nums: Vec<i32>) -> i32 {
        let mut a = 0;
        let mut b = 0;

        for num in nums {
            let max_amount = max(a + num, b);
            a = b;
            b = max_amount;
        }
        max(a, b)
    }

    if nums.len() == 1 { return nums[0]; }
    max(solve(nums[1..].to_vec()), solve(nums[0..nums.len()-1].to_vec()))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let  nums = vec![2,3,2];

        let actual = rob(nums);

        assert_eq!(actual, 3);
    }

    #[test]
    fn test_2() {
        let  nums = vec![1,2,3,1];

        let actual = rob(nums);

        assert_eq!(actual, 4);
    }

    #[test]
    fn test_3() {
        let  nums = vec![1,2,3];

        let actual = rob(nums);

        assert_eq!(actual, 3);
    }

    #[test]
    fn test_4() {
        let  nums = vec![1];

        let actual = rob(nums);

        assert_eq!(actual, 1);
    }
}
