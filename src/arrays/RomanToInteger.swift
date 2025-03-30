// https://leetcode.com/problems/roman-to-integer

import Testing

enum RomanToInteger {
    class Solution {
        let romanToInt: [Character: Int] = [
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        ]

        // Characters have a negative value only if they come out of order
        // e.g. in IV, I is less than V and therefore its value is -1 rather than 1
        func romanToInt(_ s: String) -> Int {
            var totalValue = 0

            // Operate on an array for simplicity
            let characters = Array(s)

            for i in 0 ..< characters.count {
                let currentValue = romanToInt[characters[i]]!
                let nextValue = (i < characters.count - 1)
                    ? romanToInt[characters[i + 1]]!
                    : 0

                totalValue += (currentValue < nextValue) ? -currentValue : currentValue
            }
            return totalValue
        }
    }

    struct Input {
        let s: String
    }

    struct Expected {
        let val: Int
    }

    @Test(
        "RomanToInteger",
        arguments: [
            TestData(
                id: "1",
                input: Input(s: "III"),
                expected: Expected(val: 3)
            ),
            TestData(
                id: "2",
                input: Input(s: "LVIII"),
                expected: Expected(val: 58)
            ),
            TestData(
                id: "3",
                input: Input(s: "MCMXCIV"),
                expected: Expected(val: 1994)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let output = Solution().romanToInt(
            testData.input.s
        )
        #expect(output == testData.expected.val)
    }
}
