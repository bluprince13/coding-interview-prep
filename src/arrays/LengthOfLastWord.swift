// https://leetcode.com/problems/length-of-last-word

import Foundation
import Testing

enum LengthOfLastWord {
    class Solution {
        func lengthOfLastWord(_ s: String) -> Int {
            return s.trimmingCharacters(in: .whitespaces)
                .split(separator: " ")
                .last?.count ?? 0
        }
    }

    struct Input {
        let s: String
    }

    struct Expected {
        let val: Int
    }

    @Test(
        "LengthOfLastWord",
        arguments: [
            TestData(
                id: "1",
                input: Input(s: "Hello World"),
                expected: Expected(val: 5)
            ),

            TestData(
                id: "2",
                input: Input(s: "   fly me   to   the moon  "),
                expected: Expected(val: 4)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = Solution().lengthOfLastWord(testData.input.s)
        #expect(result == testData.expected.val)
    }
}
