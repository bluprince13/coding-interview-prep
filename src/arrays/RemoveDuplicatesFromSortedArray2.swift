// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

import Testing

enum RemoveDuplicatesFromSortedArray2 {
    class Solution {
        func removeDuplicates(_ nums: inout [Int]) -> Int {
            if nums.count <= 2 {
                return nums.count
            }

            var write = 2

            for read in 2 ..< nums.count {
                if nums[read] != nums[write - 2] {
                    nums[write] = nums[read]
                    write += 1
                }
            }

            return write
        }
    }

    struct Input {
        let nums: [Int]
    }

    struct Expected {
        let nums: [Int]
        let val: Int
    }

    @Test(
        "RemoveDuplicatesFromSortedArray",
        arguments: [
            TestData(
                id: "1",
                input: Input(nums: [1, 1, 1, 2, 2, 3]),
                expected: Expected(nums: [1, 1, 2, 2, 3, 3], val: 5)
            ),
            TestData(
                id: "2",
                input: Input(nums: [0, 0, 1, 1, 1, 1, 2, 3, 3]),
                expected: Expected(nums: [0, 0, 1, 1, 2, 3, 3, 3, 3], val: 7)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        var nums = testData.input.nums
        let output = Solution().removeDuplicates(
            &nums
        )
        #expect(output == testData.expected.val)
        #expect(nums == testData.expected.nums)
    }
}
