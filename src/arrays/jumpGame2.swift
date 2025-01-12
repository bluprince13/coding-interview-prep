// https://leetcode.com/problems/jump-game-ii

import Testing

enum JumpGame2Namespace {
    static func jump(_ nums: [Int]) -> Int {
        // Intuition
        // From the current position, we get a choice of positions to jump to
        // Greedily, we will choose the one that gives us maxReach
        // We record a jump when we have got to the maxReachFromLastJump
        // Keep jumping until maxReachFromLastJump >= finalIndex
        var jumps = 0, maxReach = 0, maxReachFromLastJump = 0
        let finalIndex = nums.count - 1

        for (i, val) in nums.enumerated() where maxReachFromLastJump < finalIndex {
            maxReach = max(maxReach, i + val)

            if i == maxReachFromLastJump {
                jumps += 1
                maxReachFromLastJump = maxReach
            }
        }

        return jumps
    }

    struct Input {
        let nums: [Int]
    }

    struct Expected {
        let val: Int
    }

    @Test(
        "JumpGame2",
        arguments: [
            TestData(
                id: "1",
                input: Input(nums: [2, 3, 1, 1, 4]),
                expected: Expected(val: 2)
            ),
            TestData(
                id: "2",
                input: Input(nums: [2, 3, 0, 1, 4]),
                expected: Expected(val: 2)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = jump(testData.input.nums)
        #expect(result == testData.expected.val)
    }
}
