// https://leetcode.com/problems/simplify-path/

pub fn simplify_path(path: String) -> String {
    let elements = path.split("/");
    let mut stack = vec![""];
    for element in elements {
        if element != "" {
            stack.push(element)
        }
    }

    let length = stack.len();
    if (length > 1) & (stack[length - 1] == "/") {
        stack.pop();
    }
    stack.join("/")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn simplify_path_returns_path_1() {
        let actual = simplify_path("/home/".to_string());

        assert_eq!(actual, "/home");
    }

    fn simplify_path_returns_path_2() {
        let actual = simplify_path("/home/../src/test/".to_string());

        assert_eq!(actual, "/src/test");
    }
}
