// https://leetcode.com/problems/jump-game

import Testing

enum JumpGame {
    class Solution {
        func canJump(_ nums: [Int]) -> Bool {
            var maxReachableIndex = 0
            let finalIndex = nums.count - 1

            for (i, val) in nums.enumerated() where i <= maxReachableIndex {
                maxReachableIndex = max(maxReachableIndex, i + val)
                if maxReachableIndex >= finalIndex {
                    return true
                }
            }

            return false
        }
    }

    struct Input {
        let nums: [Int]
    }

    struct Expected {
        let val: Bool
    }

    @Test(
        "JumpGame",
        arguments: [
            TestData(
                id: "1",
                input: Input(nums: [2, 3, 1, 1, 4]),
                expected: Expected(val: true)
            ),
            TestData(
                id: "2",
                input: Input(nums: [3, 2, 1, 0, 4]),
                expected: Expected(val: false)
            ),
            TestData(
                id: "3",
                input: Input(nums: [3, 0, 8, 2, 0, 0, 1]),
                expected: Expected(val: true)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = Solution().canJump(testData.input.nums)
        #expect(result == testData.expected.val)
    }
}
