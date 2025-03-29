// https://leetcode.com/problems/majority-element

import Testing

enum MajorityElement {
    class Solution {
        func majorityElement(_ nums: [Int]) -> Int {
            // Moore's voting algorithm
            // if there is a majority element in an array, it will always remain
            // in the lead, even after encountering other elements

            var count = 0
            var candidate: Int? = nil

            for num in nums {
                if count == 0 {
                    candidate = num
                }

                count += (num == candidate ? 1 : -1)
            }

            guard let majorityCandidate = candidate else {
                fatalError("No majority element found")
            }

            return majorityCandidate
        }
    }

    struct Input {
        let nums: [Int]
    }

    struct Expected {
        let val: Int
    }

    @Test(
        "MajorityElement",
        arguments: [
            TestData(
                id: "1",
                input: Input(nums: [3, 2, 3]),
                expected: Expected(val: 3)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let output = Solution().majorityElement(
            testData.input.nums
        )
        #expect(output == testData.expected.val)
    }
}
