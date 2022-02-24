// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum

package codingInterviewPrep

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func getSum(s []int) (sum int) {
	for _, v := range s {
		sum += v
	}
	return
}

// O(n^2) - Brute force
func canThreePartsEqualSumBruteForce(arr []int) bool {
	n := len(arr)
	for i := 1; i <= n-2; i++ {
		for j := n - 1; j >= i+1; j-- {
			sum_part1 := getSum(arr[:i])
			sum_part2 := getSum(arr[i:j])
			sum_part3 := getSum(arr[j:])
			if sum_part1 == sum_part2 && sum_part2 == sum_part3 {
				return true
			}
		}
	}
	return false
}

// O(n)
// Check if we can find two indices such that sum is 1/3 and 2/3
func canThreePartsEqualSum(arr []int) bool {
	n := len(arr)
	total := getSum(arr)

	if total%3 != 0 {
		return false
	}

	oneThird := total / 3
	twoThird := oneThird * 2
	foundFirstIndex := false
	sum := 0
	for i := 0; i < n-1; i++ {
		sum += arr[i]
		if sum == oneThird && !foundFirstIndex {
			foundFirstIndex = true
			continue
		}
		if sum == twoThird && foundFirstIndex {
			return true
		}
	}
	return false
}

func TestCanThreePartsEqualSumBruteForceReturnsTrue_1(t *testing.T) {
	actual := canThreePartsEqualSumBruteForce([]int{0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1})
	assert.Equal(t, true, actual)
}

func TestCanThreePartsEqualSumBruteForceReturnsTrue_2(t *testing.T) {
	actual := canThreePartsEqualSumBruteForce([]int{3, 3, 6, 5, -2, 2, 5, 1, -9, 4})
	assert.Equal(t, true, actual)
}

func TestCanThreePartsEqualSumBruteForceReturnsFalse(t *testing.T) {
	actual := canThreePartsEqualSumBruteForce([]int{0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1})
	assert.Equal(t, false, actual)
}

func TestCanThreePartsEqualSumReturnsTrue_1(t *testing.T) {
	actual := canThreePartsEqualSum([]int{0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1})
	assert.Equal(t, true, actual)
}

func TestCanThreePartsEqualSumReturnsTrue_2(t *testing.T) {
	actual := canThreePartsEqualSum([]int{3, 3, 6, 5, -2, 2, 5, 1, -9, 4})
	assert.Equal(t, true, actual)
}

func TestCanThreePartsEqualSumReturnsTrue_3(t *testing.T) {
	actual := canThreePartsEqualSum([]int{1, -1, 1, -1})
	assert.Equal(t, false, actual)
}

func TestCanThreePartsEqualSumReturnsTrue_4(t *testing.T) {
	actual := canThreePartsEqualSum([]int{0, 0, 0, 0})
	assert.Equal(t, true, actual)
}

func TestCanThreePartsEqualSumReturnsFalse(t *testing.T) {
	actual := canThreePartsEqualSum([]int{0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1})
	assert.Equal(t, false, actual)
}
