// https://leetcode.com/problems/product-of-array-except-self

import Testing

enum ProductOfArrayExceptSelf {
    class Solution {
        func productExceptSelf(_ nums: [Int]) -> [Int] {
            let count = nums.count
            guard count > 1 else { return nums }
            
            var result = Array(repeating: 1, count: count)

            // For each index i, what's the product of all previous numbers
            var prefix = 1
            for i in 0..<count {
                // At index i, the result is a product of the prefix and ...
                result[i] = prefix
                prefix *= nums[i]
            }
            
            // For each index i, what's the product of all following numbers
            var suffix = 1
            for i in (0..<count).reversed() {
                // ... the suffix
                result[i] *= suffix
                suffix *= nums[i]
            }

            return result
        }
    }

    struct Input {
        let nums: [Int]
    }

    struct Expected {
        let val: [Int]
    }

    @Test(
        "ProductOfArrayExceptSelf",
        arguments: [
            TestData(
                id: "1",
                input: Input(nums: [1, 2, 3, 4]),
                expected: Expected(val: [24, 12, 8, 6])
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = Solution().productExceptSelf(testData.input.nums)
        #expect(result == testData.expected.val)
    }
}
