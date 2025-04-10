
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

import Testing

enum FindTheIndexOfTheFirstOccurrenceInAString {
    class Solution {
        func strStr(_ haystack: String, _ needle: String) -> Int {
            guard haystack.count >= needle.count else { return -1 }

            // At every char, check if there is a substring match
            for i in 0...(haystack.count - needle.count) {
                let start = haystack.index(haystack.startIndex, offsetBy: i)
                let end = haystack.index(start, offsetBy: needle.count)
                if haystack[start..<end] == needle {
                    return i
                }
            }

            return -1
        }
    }

    struct Input {
        let haystack: String
        let needle: String
    }

    struct Expected {
        let val: Int
    }

    @Test(
        "FindTheIndexOfTheFirstOccurrenceInAString",
        arguments: [
            TestData(
                id: "1",
                input: Input(haystack: "sadbutsad", needle: "sad"),
                expected: Expected(val: 0)
            ),
            TestData(
                id: "2",
                input: Input(haystack: "leetcode", needle: "leeto"),
                expected: Expected(val: -1)
            ),
            TestData(
                id: "3",
                input: Input(haystack: "aaa", needle: "a"),
                expected: Expected(val: 0)
            ),
            TestData(
                id: "4",
                input: Input(haystack: "aaa", needle: "aaaa"),
                expected: Expected(val: -1)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = Solution().strStr(testData.input.haystack, testData.input.needle)
        #expect(result == testData.expected.val)
    }
}
