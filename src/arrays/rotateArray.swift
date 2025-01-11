// https://leetcode.com/problems/rotate-array

import Testing

enum RotateArrayNamespace {
    static func rotate(_ nums: inout [Int], _ k: Int) {
        let numRotations = k % nums.count

        reverse(&nums[...])
        reverse(&nums[0..<numRotations])
        reverse(&nums[numRotations...])
    }

    private static func reverse(_ nums: inout ArraySlice<Int>) {
        var i = nums.startIndex
        var j = nums.endIndex - 1

        while i < j {
            nums.swapAt(i, j)
            i += 1
            j -= 1
        }
    }

    struct Input {
        let nums: [Int]
        let k: Int
    }

    struct Expected {
        let nums: [Int]
    }

    @Test(
        "RotateArray",
        arguments: [
            TestData(
                id: "1",
                input: Input(nums: [1, 2, 3, 4, 5, 6, 7], k: 3),
                expected: Expected(nums: [5, 6, 7, 1, 2, 3, 4])
            ),
            TestData(
                id: "2",
                input: Input(nums: [1, 2], k: 2),
                expected: Expected(nums: [1, 2])
            ),
            TestData(
                id: "3",
                input: Input(nums: [-1,-100,3,99], k: 2),
                expected: Expected(nums: [3,99,-1,-100])
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        var nums = testData.input.nums
        rotate(
            &nums,
            testData.input.k
        )
        #expect(nums == testData.expected.nums)
    }
}
