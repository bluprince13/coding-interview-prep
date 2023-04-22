/*
---
difficulty:
    site: medium
    perceived: hard
url: https://leetcode.com/problems/delete-and-earn
time_complexity: O(max(nums))
space_complexity: O(max(nums))
categories: [dp]
---
*/

use std::cmp::max;
use std::collections::{HashSet};

pub fn delete_and_earn_sub_optimail(nums: Vec<i32>) -> i32 {
    fn solve(nums: &[i32], mut deleted: HashSet<i32>, mut discarded: HashSet<i32>) -> i32 {
        // Base case
        if nums.is_empty(){
           return 0;
        }

        // Single path forward if already discarded or deleted
        if discarded.contains(&nums[0]) {
            return solve(&nums[1..], deleted, discarded);
        } else if deleted.contains(&nums[0]) {
            return solve(&nums[1..], deleted, discarded) + nums[0];
        }

        // Two choices if number not encountered before
        // This means time complexity is O(2^n)
        // Option 1: Discard and continue
        let option1 = solve(&nums[1..], deleted.clone(), discarded.clone());
        // Option 2: Delete and continue
        discarded.insert(nums[0] + 1);
        discarded.insert(nums[0] - 1);
        deleted.insert(nums[0]);
        max(
            option1,
            solve(&nums[1..], deleted, discarded) + nums[0],
        )
    }

    solve(&nums, HashSet::new(), HashSet::new())
}


// We can get a better performing solution by using a dynamic programming
// approach
// The following solution is O(max(nums))
// This is okay because we have a constraint nums[i] <= 10^4
// TODO: Improve time complexity even further

pub fn delete_and_earn(nums: Vec<i32>) -> i32 {
    let max_num = nums.iter().max().unwrap();
    let mut counts = vec![0; *max_num as usize + 1];

    for num in nums {
        counts[num as usize] += 1;
    }

    let mut a = 0;
    let mut b= 0;

    for (i, count) in counts.iter().enumerate() {
        let max_amount = max(a + (i * count) as i32, b);
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
        let nums = vec![3, 4, 2];

        let actual = delete_and_earn(nums);

        assert_eq!(actual, 6);
    }

    #[test]
    fn test_2() {
        let nums = vec![2, 2, 3, 3, 3, 4];

        let actual = delete_and_earn(nums);

        assert_eq!(actual, 9);
    }

    #[test]
    fn test_3() {
        let nums = vec![3, 3, 2];

        let actual = delete_and_earn(nums);

        assert_eq!(actual, 6);
    }
}
