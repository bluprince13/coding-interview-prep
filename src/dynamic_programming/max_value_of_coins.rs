// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

use std::cmp::{max, min};

// TODO: Time complexity
// TODO: Space complexity

pub fn max_value_of_coins(piles: Vec<Vec<i32>>, k: i32) -> i32 {
    let number_of_piles = piles.len();
    // dp[i][coins] is the  maximum total value of coins you can have in your
    // wallet if you choose at most coins coins from the leftmost i piles
    // optimally
    // We use a pile 0 for convenience
    // For two piles:
    // +---------+--------+---------+---------+
    // |         | pile 0 |  pile 1 |  pile 2 |
    // +---------+--------+---------+---------+
    // | 0 coins |      0 |       0 |       0 |
    // | 1 coins |      0 |       0 |       0 |
    // | 2 coins |      0 |       0 |       0 |
    // +---------+--------+---------+---------+
    let mut dp = vec![vec![0; (k + 1) as usize]; number_of_piles + 1];
    // i: [1, 2]
    for (i, current_pile) in piles.iter().enumerate() {
        let i = i + 1;

        let mut sum = 0;
        let mut sum_of_coins_in_current_pile: Vec<i32> = vec![0];
        for (coin, coin_value) in current_pile.iter().enumerate() {
            if coin > k as usize {
                break;
            }
            sum += coin_value;
            sum_of_coins_in_current_pile.push(sum);
        }

        // Iterate over each possible number of coins
        // coins: [0, 1, 2]
        for coins in 0..k + 1 {
            // Iterate over each possible number of coins from the current pile
            // e.g. when i = 1, and coins = 1
            // coins_from_current_pile: [0, 1] as 1 is min(3, 1)
            for coins_from_current_pile in 0..min(current_pile.len(), coins as usize) + 1 {
                dp[i][coins as usize] = max(
                    // previous value
                    dp[i][coins as usize],
                    // new value
                    dp[i - 1][coins as usize - coins_from_current_pile] + sum_of_coins_in_current_pile[coins_from_current_pile],
                );
            }
        }
    }
    // +---------+--------+---------+---------+
    // |         | pile 0 |  pile 1 |  pile 2 |
    // +---------+--------+---------+---------+
    // | 0 coins |      0 |       0 |       0 |
    // | 1 coins |      0 |       1 |       7 |
    // | 2 coins |      0 |     101 |      101|
    // +---------+--------+---------+---------+
    // Answer is in dp[2][2]
    dp[number_of_piles][k as usize]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let piles: Vec<Vec<i32>> = vec![vec![1, 100, 3], vec![7, 8, 9]];
        let k = 2;
        let actual = max_value_of_coins(piles, k);

        assert_eq!(actual, 101);
    }

    #[test]
    fn test_2() {
        let piles: Vec<Vec<i32>> = vec![
            vec![100],
            vec![100],
            vec![100],
            vec![100],
            vec![100],
            vec![100],
            vec![1, 1, 1, 1, 1, 1, 700],
        ];
        let k = 7;
        let actual = max_value_of_coins(piles, k);

        assert_eq!(actual, 706);
    }
}
