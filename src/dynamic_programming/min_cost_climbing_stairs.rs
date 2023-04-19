// https://leetcode.com/problems/min-cost-climbing-stairs

use std::cmp::min;

pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 { // [10, 15, 20]
    let mut a = cost[0]; // 10
    let mut b = cost[1]; // 15
    for current_step_cost in &cost[2..] { // iterate over [20]
        let min_cost = min(a, b) + current_step_cost; // 30
        a = b; // 15
        b = min_cost; // 30
    }
    min(a, b) // 15
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_0() {
        let cost =  vec![10,15];
        let actual = min_cost_climbing_stairs(cost);

        assert_eq!(actual, 10);
    }

    #[test]
    fn test_01() {
        let cost =  vec![15,10];
        let actual = min_cost_climbing_stairs(cost);

        assert_eq!(actual, 10);
    }



    #[test]
    fn test_1() {
        let cost =  vec![10,15,20];
        let actual = min_cost_climbing_stairs(cost);

        assert_eq!(actual, 15);
    }

    #[test]
    fn test_2() {
        let cost = vec![1,100,1,1,1,100,1,1,100,1];
        let actual = min_cost_climbing_stairs(cost);

        assert_eq!(actual, 6);
    }
}
