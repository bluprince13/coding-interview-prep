import Testing

enum IntegerToRoman {
    class Solution {
        let romanNumerals: [(value: Int, symbol: String)] = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        func intToRoman(_ num: Int) -> String {
            var remainder = num
            var result = ""

            for (value, symbol) in romanNumerals {
                while remainder >= value {
                    remainder -= value
                    result.append(symbol)
                }
            }
            return result
        }
    }

    struct Input {
        let num: Int
    }

    struct Expected {
        let val: String
    }

    @Test(
        "IntegerToRoman",
        arguments: [
            TestData(
                id: "1",
                input: Input(num: 3749),
                expected: Expected(val: "MMMDCCXLIX")
            ),
            TestData(
                id: "2",
                input: Input(num: 58),
                expected: Expected(val: "LVIII")
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = Solution().intToRoman(testData.input.num)
        #expect(result == testData.expected.val)
    }
}
