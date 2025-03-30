// https://leetcode.com/problems/longest-common-prefix

import Testing

enum LongestCommonPrefix {
    class Solution {
        func longestCommonPrefix(_ strs: [String]) -> String {
            var prefix = strs.first ?? ""
            for s in strs {
                prefix = commonPrefix(prefix, s)
            }
            return prefix
        }

        private func commonPrefix(_ a: String, _ b: String) -> String {
            var prefix = ""

            for (aChar, bChar) in zip(a, b) {
                if aChar == bChar {
                    prefix.append(aChar)
                } else {
                    break
                }
            }

            return prefix
        }
    }

    struct Input {
        let strs: [String]
    }

    struct Expected {
        let val: String
    }

    @Test(
        "LongestCommonPrefix",
        arguments: [
            TestData(
                id: "1",
                input: Input(strs: ["flower", "flow", "flight"]),
                expected: Expected(val: "fl")
            ),

            TestData(
                id: "2",
                input: Input(strs: ["dog", "racecar", "car"]),
                expected: Expected(val: "")
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = Solution().longestCommonPrefix(testData.input.strs)
        #expect(result == testData.expected.val)
    }
}
