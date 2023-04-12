// https://leetcode.com/problems/simplify-path/

pub fn simplify_path(path: String) -> String {
    let elements = path.split("/");
    let mut stack = vec![""];
    for element in elements {
        if element == ".." {
            if stack.len() > 1 {
                stack.pop();
            };
        } else if (element != "") && (element != ".") {
            stack.push(element)
        }
    }

    if stack.len() == 1 {
        stack.push("");
    }

    stack.join("/")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn simplify_path_removes_trailing_slash() {
        let actual = simplify_path("/home/".to_string());

        assert_eq!(actual, "/home");
    }

    #[test]
    fn simplify_path_handles_initial_double_period() {
        let actual = simplify_path("/../".to_string());

        assert_eq!(actual, "/");
    }

    #[test]
    fn simplify_path_handles_later_double_period() {
        let actual = simplify_path("/home/../".to_string());

        assert_eq!(actual, "/");
    }

    #[test]
    fn simplify_path_handles_period() {
        let actual = simplify_path("/.".to_string());

        assert_eq!(actual, "/");
    }

    #[test]
    fn simplify_path_handles_multiple_slash() {
        let actual = simplify_path("home//foo".to_string());

        assert_eq!(actual, "/home/foo");
    }

    #[test]
    fn simplify_path_handles_complex_input() {
        let actual = simplify_path("home/../src//./test/".to_string());

        assert_eq!(actual, "/src/test");
    }
}
