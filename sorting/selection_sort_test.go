package codingInterviewPrep

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func SelectionSort(nums []int) []int {
	n := len(nums)
	for i := range nums {
		min := i
		for j := i + 1; j < n; j++ {
			if nums[j] < nums[min] {
				min = j
			}
		}
		nums[i], nums[min] = nums[min], nums[i]
	}
	return nums
}

func TestSelectionSort(t *testing.T) {
	nums := []int{2, 4, 1}
	actual := SelectionSort(nums)
	expected := []int{1, 2, 4}
	assert.Equal(t, expected, actual)
}
