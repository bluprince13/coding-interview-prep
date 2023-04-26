/*
---
difficulty:
    site: medium
    perceived: hard
url: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product
time_complexity: O(n)
space_complexity: 1
categories: [dp]
resources: []
---
*/

use std::cmp::max;

// zeros are a natural breakpoint where length is reset to 0
// Even numbers of negative numbers could be part of the subarray
// However, given an odd numbers of negative numbers, the first or last one
// won't count

pub fn get_max_len(nums: Vec<i32>) -> i32 {
    let mut postive_product_length = 0;
    let mut negative_product_length = 0;
    let mut max_length = 0;
    for num in &nums {
        match num {
            // Break at zeros
            0 => {
                postive_product_length = 0;
                negative_product_length = 0;
            }
            // When positive, postive_product_length is incremented
            // However, we can only increment negative_product_length if there
            // was already a negative number
            x if x > &0 => {
                postive_product_length += 1;
                negative_product_length = match negative_product_length {
                    0 => 0,
                    _ => negative_product_length + 1,
                };
            }
            // When we encounter a negative number, we have to swap the counts
            // Example:
            // [1, 2]
            //      positive = 2
            //      negative = 0
            // [1, 2, -3]
            //      SWAP HERE
            //      positive = 0
            //      negative = 3
            // [1, 2, -3, 4]
            //      positive = 1
            //      negative = 4
            // [1, 2, -3, 4, -5]
            //      SWAP HERE
            //      positive = 5
            //      negative = 2
            // Every time we hit an even number of negative numbers, positive
            // will become the length of the array - which is what we want.
            _ => {
                let temp = postive_product_length;
                postive_product_length = match negative_product_length {
                    0 => 0,
                    _ => negative_product_length + 1,
                };
                negative_product_length = temp + 1;
            }
        }
        max_length = max(postive_product_length, max_length);
    }
    max_length
}

#[cfg(test)]

mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let nums = vec![1, -2, -3, 4];

        let actual = get_max_len(nums);

        assert_eq!(actual, 4);
    }

    #[test]
    fn test_2() {
        let nums = vec![0, 1, -2, -3, -4];

        let actual = get_max_len(nums);

        assert_eq!(actual, 3);
    }

    #[test]
    fn test_3() {
        let nums = vec![-1, -2, -3, 0, 1];

        let actual = get_max_len(nums);

        assert_eq!(actual, 2);
    }

    #[test]
    fn test_4() {
        let nums = vec![1, -2, 3, 0, 1];

        let actual = get_max_len(nums);

        assert_eq!(actual, 1);
    }

    #[test]
    fn test_5() {
        let nums = vec![-1, 2];

        let actual = get_max_len(nums);

        assert_eq!(actual, 1);
    }
}
