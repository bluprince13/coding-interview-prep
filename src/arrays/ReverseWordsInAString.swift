// https://leetcode.com/problems/reverse-words-in-a-string

import Foundation
import Testing

enum ReverseWordsInAString {
    class Solution {
        func reverseWords(_ s: String) -> String {
            return s.trimmingCharacters(in: .whitespaces)
                .split(separator: " ")
                .reversed()
                .joined(separator: " ")
        }
    }

    struct Input {
        let s: String
    }

    struct Expected {
        let val: String
    }

    @Test(
        "ReverseWordsInAString",
        arguments: [
            TestData(
                id: "1",
                input: Input(s: "the sky is blue"),
                expected: Expected(val: "blue is sky the")
            ),
            TestData(
                id: "2",
                input: Input(s: "  hello world  "),
                expected: Expected(val: "world hello")
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = Solution().reverseWords(testData.input.s)
        #expect(result == testData.expected.val)
    }
}
