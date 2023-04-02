fn say_hello(name: &str) -> String {
    let hello_string = format!("Hello, {}", name);
    return hello_string;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn say_hello_returns_hello_string() {
        let actual = say_hello("Vipin");

        assert_eq!(actual, "Hello, Vipin");
    }
}
