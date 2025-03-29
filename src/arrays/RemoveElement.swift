// https://leetcode.com/problems/remove-element

import Testing

enum RemoveElement {
    class Solution {
        func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
            var i = 0
            var j = nums.count - 1

            while i <= j {
                // Do the check at i
                // If jth position also has val, it will be handled in the next iteration
                if nums[i] == val {
                    nums[i] = nums[j]
                    j -= 1
                } else {
                    i += 1
                }
            }

            return i
        }
    }

    struct Input {
        let nums: [Int]
        let val: Int
    }

    struct Expected {
        let nums: [Int]
        let val: Int
    }

    @Test(
        "RemoveElement",
        arguments: [
            TestData(
                id: "standard",
                input: Input(nums: [3, 2, 2, 3], val: 2),
                expected: Expected(nums: [3, 3, 2, 3], val: 2)
            ),
            TestData(
                id: "empty",
                input: Input(nums: [], val: 3),
                expected: Expected(nums: [], val: 0)
            ),
            TestData(
                id: "single",
                input: Input(nums: [3], val: 3),
                expected: Expected(nums: [3], val: 0)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        var nums = testData.input.nums
        let output = Solution().removeElement(
            &nums,
            testData.input.val
        )
        #expect(output == testData.expected.val)
        #expect(nums == testData.expected.nums)
    }
}
