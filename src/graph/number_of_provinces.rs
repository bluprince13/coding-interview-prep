/*
---
difficulty:
    site:
    perceived:
url: https://leetcode.com/problems/number-of-provinces/
time_complexity:
space_complexity:
categories: [graph]
resources: []
---
*/

pub fn find_circle_num(is_connected: Vec<Vec<i32>>) -> i32 {
    let visited = vec![false, is_connected.len()];
    for i, city in is_connected.iter().enumerate() {
        for j, _ in city.iter().enumerate() {

        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let is_connected = vec![vec![1, 1, 0], vec![1, 1, 0], vec![0, 0, 1]];
        let actual = find_circle_num(is_connected);

        assert_eq!(actual, 2);
    }

    #[test]
    fn test_2() {
        let is_connected = vec![vec![1, 0, 0], vec![0, 1, 0], vec![0, 0, 1]];
        let actual = find_circle_num(is_connected);

        assert_eq!(actual, 3);
    }
}
