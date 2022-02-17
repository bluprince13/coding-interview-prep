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

func InsertionSort(nums []int) []int {
	for i, value := range nums {
		key := value
		j := i - 1
		for j >= 0 && nums[j] > key {
			nums[j+1] = nums[j]
			j--
		}
		nums[j+1] = key
	}
	return nums
}

func TestSelectionSort(t *testing.T) {
	nums := []int{3, 2, 1}
	actual := SelectionSort(nums)
	expected := []int{1, 2, 3}
	assert.Equal(t, expected, actual)
}

func TestInsertionSort(t *testing.T) {
	nums := []int{3, 2, 1}
	actual := InsertionSort(nums)
	expected := []int{1, 2, 3}
	assert.Equal(t, expected, actual)
}
