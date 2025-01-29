// https://leetcode.com/problems/h-index

import Testing

enum HIndexNamespace {
    static func hIndex(_ citations: [Int]) -> Int {
        let numberOfPapers = citations.count

        // Get the frequency for each number of citations
        // hIndex must be <= numberOfPapers
        // If any paper has more citations than numberOfPapers
        // Then we put that in the last frequency bucket
        var frequencies = Array(repeating: 0, count: numberOfPapers + 1)
        for citation in citations {
            let index = min(citation, numberOfPapers)
            frequencies[index] += 1
        }

        var cumulativeFrequency = 0
        for citation in (0 ..< frequencies.count).reversed() {
            let frequencyOfCitation = frequencies[citation]
            cumulativeFrequency += frequencyOfCitation
            if cumulativeFrequency >= citation {
                return citation
            }
        }
        return 0
    }

    struct Input {
        let nums: [Int]
    }

    struct Expected {
        let val: Int
    }

    @Test(
        "HIndex",
        arguments: [
            TestData(
                id: "1",
                input: Input(nums: [3, 0, 6, 1, 5]),
                expected: Expected(val: 3)
            ),
            TestData(
                id: "2",
                input: Input(nums: [1, 3, 1]),
                expected: Expected(val: 1)
            )
        ]
    )
    static func test(testData: TestData<Input, Expected>) {
        let result = hIndex(testData.input.nums)
        #expect(result == testData.expected.val)
    }
}
