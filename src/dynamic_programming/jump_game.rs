/*
---
difficulty:
    site: medium
    perceived: hard
url: https://leetcode.com/problems/jump-game
time_complexity: O(n)
space_complexity: O(1)
categories: [dp]
---
*/

use std::cmp::max;

pub fn can_jump(nums: Vec<i32>) -> bool {
    let last_index = nums.len() - 1;
    let mut maximum = 0;
    let mut i = 0;
    while i <= maximum {
        maximum = max(maximum, i + nums[i] as usize);
        i += 1;
        if maximum >= last_index { return true };
    }
    false
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let nums = vec![2,3,1,1,4];

        let actual = can_jump(nums);

        assert!(actual);
    }

    #[test]
    fn test_2() {
        let nums = vec![3,2,1,0,4];

        let actual = can_jump(nums);

        assert!(!actual);
    }
}
