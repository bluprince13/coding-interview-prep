// https://leetcode.com/problems/validate-stack-sequences/

pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
    let mut stack: Vec<i32> = vec![];
    let mut i = 0;
    let mut j = 0;
    let max_i = pushed.len() - 1;
    let max_j = popped.len() - 1;
    while j <= max_j {
        // We have to either do a push, or a pop until we have iterated through
        // the popped vector
        // If we can't push/pop, then we can just return false
        if !stack.is_empty() && stack[stack.len() - 1] == popped[j] {
            stack.pop();
            j += 1;
        } else if i <= max_i {
            stack.push(pushed[i]);
            i += 1;
        } else {
            return false
        }
    }
    true
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn validate_stack_sequences_happy_path() {
        let pushed = vec![1, 2, 3, 4, 5];
        let popped = vec![4, 5, 3, 2, 1];
        let actual = validate_stack_sequences(pushed, popped);

        assert!(actual);
    }

    #[test]
    fn validate_stack_sequences_unhappy_path() {
        let pushed = vec![1, 2, 3, 4, 5];
        let popped = vec![4, 3, 5, 1, 2];
        let actual = validate_stack_sequences(pushed, popped);

        assert!(!actual);
    }

    #[test]
    fn validate_stack_sequences_3() {
        let pushed = vec![1, 2, 3, 0];
        let popped = vec![2, 1, 3, 0];
        let actual = validate_stack_sequences(pushed, popped);

        assert!(actual);
    }
}
