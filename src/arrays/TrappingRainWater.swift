// https://leetcode.com/problems/trapping-rain-water

import Testing

enum TrappingRainWater {
    class Solution {
        // Water at any point is determined by:
        // 1 - max height to the left
        // 2 - max height to the right
        // 3 - height at that point
        // We could have a maxLeft and maxRight array, but this would be O(N) space
        // Instead a 2-pointer approach allows O(1) space
        func trap(_ height: [Int]) -> Int {
            var i = 0, j = height.count - 1
            var water = 0
            var leftMax = height[i], rightMax = height[j]

            while i < j {
                if leftMax < rightMax {
                    water += leftMax - height[i]

                    i += 1
                    leftMax = max(leftMax, height[i])
                } else {
                    water += rightMax - height[j]

                    j -= 1
                    rightMax = max(rightMax, height[j])
                }
            }

            return water
        }
    }

    struct Input {
        let height: [Int]
    }

    struct Expected {
        let val: Int
    }

    @Test(
        "TrappingRainWater",
        arguments: [
            TestData(
                id: "1",
                input: Input(height: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]),
                expected: Expected(val: 6)
            ),
            TestData(
                id: "2",
                input: Input(height: [4, 2, 0, 3, 2, 5]),
                expected: Expected(val: 9)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let output = Solution().trap(
            testData.input.height
        )
        #expect(output == testData.expected.val)
    }
}
