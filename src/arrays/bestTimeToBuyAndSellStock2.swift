
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

import Testing

enum BestTimeToBuyAndSellStock2Namespace {
    static func maxProfit(_ prices: [Int]) -> Int {
        var profit = 0
        for i in 0..<prices.count - 1 {
            if prices[i + 1] > prices[i] {
                profit += prices[i + 1] - prices[i]
            }
        }
        return profit
    }

    struct Input {
        let nums: [Int]
    }

    struct Expected {
        let val: Int
    }

    @Test(
        "BestTimeToBuyAndSellStock2",
        arguments: [
            TestData(
                id: "1",
                input: Input(nums: [7, 1, 5, 3, 6, 4]),
                expected: Expected(val: 7)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = maxProfit(testData.input.nums)
        #expect(result == testData.expected.val)
    }
}
