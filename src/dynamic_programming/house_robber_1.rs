/*
---
difficulty:
    site: medium
    perceived: easy
url: https://leetcode.com/problems/house-robber
time_complexity: O(n);
space_complexity: 1;
categories: [dp]
---
*/

use std::cmp::max;

// Amount from house i is max(amount from house i-2 + amount from house i, amount from house i-1)

pub fn rob(nums: Vec<i32>) -> i32 {
    let mut a = 0;
    let mut b = 0;

    for num in nums {
        let max_amount = max(a + num, b);
        a = b;
        b = max_amount;
    }
    max(a, b)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let  nums = vec![1,2,3,1];

        let actual = rob(nums);

        assert_eq!(actual, 4);
    }

    #[test]
    fn test_2() {
        let  nums = vec![2,7,9,3,1];

        let actual = rob(nums);

        assert_eq!(actual, 12);
    }
}
