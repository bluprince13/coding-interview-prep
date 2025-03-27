// https://leetcode.com/problems/gas-station

import Testing

enum GasStationNamespace {
    class Solution {
        static func canCompleteCircuit(_ gas: [Int], _ cost: [Int]) -> Int {
            let totalGas = gas.reduce(0, +)
            let totalCost = cost.reduce(0, +)
            if totalGas < totalCost {
                return -1
            }

            var gasRemaining = 0
            let numOfStations = gas.count
            var startingStation = 0

            for i in 0 ..< numOfStations {
                gasRemaining += gas[i] - cost[i]

                if gasRemaining < 0 {
                    startingStation = i + 1
                    gasRemaining = 0
                }
            }

            return startingStation
        }
    }

    struct Input {
        let gas: [Int]
        let cost: [Int]
    }

    struct Expected {
        let val: Int
    }

    @Test(
        "GasStation",
        arguments: [
            TestData(
                id: "success",
                input: Input(gas: [1, 2, 3, 4, 5], cost: [3, 4, 5, 1, 2]),
                expected: Expected(val: 3)
            ),
            TestData(
                id: "failure",
                input: Input(gas: [2, 3, 4], cost: [3, 4, 3]),
                expected: Expected(val: -1)
            ),
            TestData(
                id: "edge",
                input: Input(gas: [3, 1, 1], cost: [1, 2, 2]),
                expected: Expected(val: 0)
            ),
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let output = Solution.canCompleteCircuit(
            testData.input.gas,
            testData.input.cost
        )
        #expect(output == testData.expected.val)
    }
}
