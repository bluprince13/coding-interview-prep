import Testing

func sayHello(name: String) -> String {
    return "Hello \(name)"
}

struct TestData<Input, Expected> {
    let id: String
    let input: Input
    let expected: Expected
}


@Test(
  "Given different payment type, should display correct alert",
  arguments: [
    TestData(id: "boy name", input: "Vipin", expected: "Hello Vipin"),
    TestData(id: "girl name", input: "Geethu", expected: "Hello Geethu")
  ]
)
func test(testData: TestData<String, String>) {
    let result = sayHello(name: testData.input)
    #expect(result == testData.expected)
}
