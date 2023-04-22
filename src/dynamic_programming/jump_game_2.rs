/*
---
difficulty:
    site: medium
    perceived: hard
url: https://leetcode.com/problems/jump-game-ii
time_complexity: O(n)
space_complexity: O(1)
categories: [dp]
---
*/

use std::cmp::max;

// e.g. [2,3,1,1,4]
pub fn jump(nums: Vec<i32>) -> i32 {
    let mut number_of_jumps = 0;
    let mut current_jump_max_reach = 0;
    // first jump has to be at index 0
    let mut current_jump_max_start = 0;

    // iterate through the nums [2,3,1,1]
    // the last element is skipped as we don't need to jump again from there
    for (i, num) in nums[..nums.len() - 1].iter().enumerate() {
        // update how far we can get to in this jump
        // max(0, 0 + 2) = 2
        current_jump_max_reach = max(current_jump_max_reach, i as i32 + num);

        // if we are at the end of the starting range of this jump
        // we are forced to do the jump somewhere in that starting range
        // the starting range limit for the next jump is the max reach of this jump
        if i == current_jump_max_start as usize {
            number_of_jumps += 1; // 1
            current_jump_max_start = current_jump_max_reach; // 2
        }
    }
    number_of_jumps
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_0() {
        let nums = vec![2,3,1];

        let actual = jump(nums);

        assert_eq!(actual, 1);
    }

    #[test]
    fn test_1() {
        let nums = vec![2,3,1,1,4];

        let actual = jump(nums);

        assert_eq!(actual, 2);
    }

    #[test]
    fn test_2() {
        let nums = vec![2,3,0,1,4];

        let actual = jump(nums);

        assert_eq!(actual, 2);
    }

    #[test]
    fn test_3() {
        let nums = vec![2,4,1,0,4];

        let actual = jump(nums);

        assert_eq!(actual, 2);
    }
}
