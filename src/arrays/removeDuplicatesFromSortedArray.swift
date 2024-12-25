// https://leetcode.com/problems/remove-duplicates-from-sorted-array

import Testing

enum RemoveDuplicatesFromSortedArrayNamespace {
    static func removeDuplicates(_ nums: inout [Int]) -> Int {
        var write = 0

        for read in 0 ..< nums.count {
            if read != write && nums[read] != nums[write] {
                write += 1
                nums[write] = nums[read]
            }
        }

        return write + 1
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
                input: Input(nums: [1, 1, 2]),
                expected: Expected(nums: [1, 2, 2], val: 2)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        var nums = testData.input.nums
        let output = removeDuplicates(
            &nums
        )
        #expect(output == testData.expected.val)
        #expect(nums == testData.expected.nums)
    }
}
