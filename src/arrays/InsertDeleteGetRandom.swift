// https://leetcode.com/problems/insert-delete-getrandom-o1

import Testing

enum InsertDeleteGetRandomNamespace {
    class RandomizedSet {
        var numbers: [Int]
        var numberIndices: [Int: Int]

        init() {
            numbers = []
            numberIndices = [:]
        }

        func insert(_ val: Int) -> Bool {
            guard numberIndices[val] == nil else {
                return false
            }
            numbers.append(val)
            numberIndices[val] = numbers.count - 1
            return true
        }

        func remove(_ val: Int) -> Bool {
            guard let index = numberIndices[val] else {
                return false
            }

            let lastElement = numbers.removeLast()
            if val != lastElement {
                numbers[index] = lastElement
                numberIndices[lastElement] = index
            }

            numberIndices.removeValue(forKey: val)
            return true
        }

        func getRandom() -> Int {
            numbers.randomElement()!
        }
    }

    @Test
    static func test() {
        let set = RandomizedSet()
        #expect(set.insert(1) == true)
        #expect(set.remove(2) == false)
        #expect(set.insert(2) == true)
        #expect([1, 2].contains(set.getRandom()))
        #expect(set.remove(1) == true)
        #expect(set.insert(2) == false)
        #expect(set.getRandom() == 2)
    }
}
