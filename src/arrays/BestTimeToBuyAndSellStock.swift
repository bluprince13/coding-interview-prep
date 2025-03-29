// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

import Testing

enum BestTimeToBuyAndSellStock {
    class Solution {
        func maxProfit(_ prices: [Int]) -> Int {
            var minPrice = prices[0]
            var maxProfit = 0
            for price in prices {
                minPrice = min(price, minPrice)
                let profit = price - minPrice
                maxProfit = max(profit, maxProfit)
            }
            return maxProfit
        }
    }

    struct Input {
        let nums: [Int]
    }

    struct Expected {
        let val: Int
    }

    @Test(
        "BestTimeToBuyAndSellStock",
        arguments: [
            TestData(
                id: "1",
                input: Input(nums: [7, 1, 5, 3, 6, 4]),
                expected: Expected(val: 5)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = Solution().maxProfit(testData.input.nums)
        #expect(result == testData.expected.val)
    }
}
