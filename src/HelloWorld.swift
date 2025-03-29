import Testing

// This TestData struct is used by all the Swift tests
struct TestData<Input, Expected> {
    let id: String
    let input: Input
    let expected: Expected
}

enum HelloWorld {
    class Solution {
        func sayHello(name: String) -> String {
            return "Hello \(name)"
        }
    }

    struct Input {
        let val: String
    }

    struct Expected {
        let val: String
    }

    @Test(
        "Given different payment type, should display correct alert",
        arguments: [
            TestData(
                id: "boy name",
                input: Input(val: "Vipin"),
                expected: Expected(val: "Hello Vipin")
            ),
            TestData(
                id: "girl name",
                input: Input(val: "Geethu"),
                expected: Expected(val: "Hello Geethu")
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = Solution().sayHello(name: testData.input.val)
        #expect(result == testData.expected.val)
    }
}
