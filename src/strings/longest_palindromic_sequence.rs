// https://leetcode.com/problems/longest-palindromic-subsequence/

use std::cmp::max;
use std::collections::HashMap;

// TODO: Implement a DP approach which would be faster

pub fn  longest_palindrome_subseq(s: String) -> i32 {
    fn solve<'a>(s: &'a str, cache: &mut HashMap<&'a str, i32> ) -> i32 {
        if let Some(&result) = cache.get(s) {
            return result;
        }

        let length = s.len();
        if length < 2 {
            return length as i32;
        }

        let first_letter = &s[..1];
        let last_letter = &s[length-1..];
        let solution =
            if first_letter == last_letter {
                2 + solve(&s[1..length-1], cache)
            } else {
                max(
                    solve(&s[1..length], cache),
                    solve(&s[..length-1], cache),
                )
            };
        cache.insert(&s, solution);
        solution
    }

    let mut cache: HashMap<&str, i32> = HashMap::new();
    solve(&s, &mut cache)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_empty() {
        let actual = longest_palindrome_subseq("".to_string());

        assert_eq!(actual, 0);
    }

    #[test]
    fn test_single() {
        let actual = longest_palindrome_subseq("a".to_string());

        assert_eq!(actual, 1);
    }

    #[test]
    fn test_double_not_same() {
        let actual = longest_palindrome_subseq("ab".to_string());

        assert_eq!(actual, 1);
    }

    #[test]
    fn test_double_same() {
        let actual = longest_palindrome_subseq("aa".to_string());

        assert_eq!(actual, 2);
    }

    #[test]
    fn test_triple() {
        let actual = longest_palindrome_subseq("aba".to_string());

        assert_eq!(actual, 3);
    }

    #[test]
    fn test_1() {
        let actual = longest_palindrome_subseq("bbbab".to_string());

        assert_eq!(actual, 4);
    }

    #[test]
    fn test_2() {
        let actual = longest_palindrome_subseq("cbbd".to_string());

        assert_eq!(actual, 2);
    }
}
