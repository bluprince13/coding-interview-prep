// https://leetcode.com/problems/candy

import Testing

enum CandyNamespace {
    class Solution {
        // We could create a new array candy, and
        // traverse rating array twice - left and right
        // to ensure the requirement is met on the candy array
        // in both directions. This would be O(N) time and O(N) space.
        static func candy(_ ratings: [Int]) -> Int {
            let totalCount = ratings.count
            var candy = Array(repeating: 1, count: totalCount)

            // forward pass
            for i in 1 ..< totalCount where ratings[i] > ratings[i-1] {
                candy[i] = candy[i-1] + 1
            }

            // reverse pass
            for i in (0 ..< totalCount-1).reversed() where ratings[i] > ratings[i + 1] {
                candy[i] = max(candy[i], candy[i + 1] + 1)
            }

            return candy.reduce(0, +)
        }

        static func candyOptimised(_ ratings: [Int]) -> Int {
            let totalCount = ratings.count
            var candyCount = totalCount

            var i = 1
            while i < totalCount {
                // level
                if ratings[i] == ratings[i-1] {
                    i += 1
                    continue
                }

                // climbing
                var peak = 0
                while i < totalCount && ratings[i] > ratings[i-1] {
                    peak += 1
                    candyCount += peak
                    i += 1
                }

                // descending
                var valley = 0
                while i < totalCount && ratings[i] < ratings[i-1] {
                    valley += 1
                    candyCount += valley
                    i += 1
                }

                // adjust for double counting if both peak and valley exist
                candyCount -= min(peak, valley)
            }

            return candyCount
        }
    }

    struct Input {
        let ratings: [Int]
    }

    struct Expected {
        let val: Int
    }

    static let testArguments = [
        TestData(
            id: "1",
            input: Input(ratings: [1, 0, 2]),
            expected: Expected(val: 5)
        ),
        TestData(
            id: "2",
            input: Input(ratings: [1, 2, 2]),
            expected: Expected(val: 4)
        ),
        TestData(
            id: "peak+valley double count",
            input: Input(ratings: [1, 3, 2, 2, 1]),
            expected: Expected(val: 7)
        ),
    ]

    @Test(
        "Candy",
        arguments: testArguments
    )
    static func test(testData: TestData<Input, Expected>) {
        let output = Solution.candy(
            testData.input.ratings
        )
        #expect(output == testData.expected.val)
    }

    @Test(
        "CandyOptimised",
        arguments: testArguments
    )
    static func testOptimised(testData: TestData<Input, Expected>) {
        let output = Solution.candyOptimised(
            testData.input.ratings
        )
        #expect(output == testData.expected.val)
    }
}
