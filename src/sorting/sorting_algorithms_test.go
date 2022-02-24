package codingInterviewPrep

import (
	"math/rand"
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

func merge(a []int, b []int) []int {
	i := 0
	j := 0
	var c []int

	for i < len(a) && j < len(b) {
		if a[i] < b[j] {
			c = append(c, a[i])
			i++
		} else {
			c = append(c, b[j])
			j++
		}
	}

	for i < len(a) {
		c = append(c, a[i])
		i++
	}

	for j < len(b) {
		c = append(c, b[j])
		j++
	}

	return c
}

func MergeSort(nums []int) []int {
	if len(nums) < 2 {
		return nums
	}
	mid := len(nums) / 2
	left := MergeSort(nums[:mid])
	right := MergeSort(nums[mid:])
	return merge(left, right)
}

func partition(nums []int, low int, high int) int {
	i := low
	pivot := nums[high]
	for j := low; j < high; j++ {
		if nums[j] <= pivot {
			nums[i], nums[j] = nums[j], nums[i]
			i++
		}
	}
	nums[i], nums[high] = nums[high], nums[i]
	return i
}

// https://www.hackerrank.com/challenges/quicksort1/
func QuickSort(nums []int, low int, high int) []int {
	if low < high {
		pivot := partition(nums, low, high)
		QuickSort(nums, low, pivot-1)
		QuickSort(nums, pivot+1, high)
	}
	return nums
}

func TestSelectionSort(t *testing.T) {
	nums := []int{3, 2, 1, 5, 0}
	actual := SelectionSort(nums)
	expected := []int{0, 1, 2, 3, 5}
	assert.Equal(t, expected, actual)
}

func TestInsertionSort(t *testing.T) {
	nums := []int{3, 2, 1, 5, 0}
	actual := InsertionSort(nums)
	expected := []int{0, 1, 2, 3, 5}
	assert.Equal(t, expected, actual)
}

func TestMergeSort(t *testing.T) {
	nums := []int{3, 2, 1, 5, 0}
	actual := MergeSort(nums)
	expected := []int{0, 1, 2, 3, 5}
	assert.Equal(t, expected, actual)
}

func TestPartition(t *testing.T) {
	nums := []int{3, 2, 0, 5, 1}
	actual := partition(nums, 0, len(nums)-1)
	expected := 1
	assert.Equal(t, expected, actual)
	assert.Equal(t, []int{0, 1, 3, 5, 2}, nums)
}

func TestQuickSort(t *testing.T) {
	nums := []int{3, 2, 1, 5, 0}
	actual := QuickSort(nums, 0, len(nums)-1)
	expected := []int{0, 1, 2, 3, 5}
	assert.Equal(t, expected, actual)
}

func BenchmarkSelectionSort(b *testing.B) {
	nums := rand.Perm(100000)
	for i := 0; i < b.N; i++ {
		SelectionSort(nums)
	}
}

func BenchmarkInsertionSort(b *testing.B) {
	nums := rand.Perm(100000)
	for i := 0; i < b.N; i++ {
		InsertionSort(nums)
	}
}

func BenchmarkMergeSort(b *testing.B) {
	nums := rand.Perm(100000)
	for i := 0; i < b.N; i++ {
		MergeSort(nums)
	}
}

func BenchmarkQuickSort(b *testing.B) {
	nums := rand.Perm(100000)
	for i := 0; i < b.N; i++ {
		QuickSort(nums, 0, len(nums) - 1)
	}
}