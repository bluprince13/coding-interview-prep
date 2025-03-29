// https://leetcode.com/problems/merge-sorted-array

import Testing

enum MergeSortedArray {
    class Solution {
        func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
            // Merge from largest/back of nums1 to avoid overwriting elements in nums1
            var nums1Index = m - 1 // Pointer for element in nums1 to compare
            var nums2Index = n - 1 // Pointer for element in nums2 to compare
            var mergeIndex = m + n - 1 // Pointer for element in nums1 to write to

            while nums1Index >= 0, nums2Index >= 0 {
                if nums1[nums1Index] > nums2[nums2Index] {
                    nums1[mergeIndex] = nums1[nums1Index]
                    nums1Index -= 1
                } else {
                    nums1[mergeIndex] = nums2[nums2Index]
                    nums2Index -= 1
                }
                mergeIndex -= 1
            }

            while nums2Index >= 0 {
                nums1[mergeIndex] = nums2[nums2Index]
                nums2Index -= 1
                mergeIndex -= 1
            }
        }
    }

    struct Input {
        let nums1: [Int]
        let m: Int
        let nums2: [Int]
        let n: Int
    }

    @Test(
        "Merge",
        arguments: [
            TestData(
                id: "1",
                input: Input(nums1: [1, 2, 3, 0, 0, 0], m: 3, nums2: [2, 5, 6], n: 3),
                expected: [1, 2, 2, 3, 5, 6]
            )
        ]
    )
    static func test(testData: TestData<Input, [Int]>) {
        var nums1 = testData.input.nums1
        Solution().merge(
            &nums1,
            testData.input.m,
            testData.input.nums2,
            testData.input.n
        )
        #expect(nums1 == testData.expected)
    }
}
