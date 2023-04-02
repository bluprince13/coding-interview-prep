// https://leetcode.com/problems/binary-tree-coloring-game/

package codingInterviewPrep

import (
	"testing"

	"github.com/google/go-cmp/cmp"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func btreeGameWinningMove(root *TreeNode, n int, x int) bool {
	xNode := getNode(root, x)
	leftChildCount := countTreeNodes(xNode.Left)
	rightChildCount := countTreeNodes(xNode.Right)
	parentCount := n - (leftChildCount + rightChildCount + 1)
	return isOneNumberGreaterThanSumOfOtherTwo(leftChildCount, rightChildCount, parentCount)
}

func isOneNumberGreaterThanSumOfOtherTwo(a int, b int, c int) bool {
	if (a > b+c) || (b > a+c) || (c > a+b) {
		return true
	}
	return false
}

func countTreeNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return countTreeNodes(root.Left) + countTreeNodes(root.Right) + 1
}

func getNode(root *TreeNode, x int) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Val == x {
		return root
	}
	left := getNode(root.Left, x)
	if left != nil {
		return left
	}
	right := getNode(root.Right, x)
	if right != nil {
		return right
	}
	return nil
}

// TESTING:

func buildTree(n int, val int) *TreeNode {
	if n == 0 {
		return nil
	}

	root := &TreeNode{Val: val}
	leftVal := val * 2
	rightVal := val*2 + 1

	if leftVal <= n {
		root.Left = buildTree(n, leftVal)
		if rightVal <= n {
			root.Right = buildTree(n, rightVal)
		}
	}

	return root
}

func TestCountTreeNodes(t *testing.T) {
	testdata := map[string]struct {
		root *TreeNode
		want int
	}{
		"zero case":    {root: buildTree(0, 1), want: 0},
		"one case":     {root: buildTree(1, 1), want: 1},
		"general case": {root: buildTree(5, 1), want: 5},
	}

	for name, tc := range testdata {
		t.Run(name, func(t *testing.T) {
			got := countTreeNodes(tc.root)
			diff := cmp.Diff(tc.want, got)
			if diff != "" {
				t.Fatalf(diff)
			}
		})
	}
}

func TestBtreeGameWinningMove(t *testing.T) {
	testdata := map[string]struct {
		root *TreeNode
		n    int
		x    int
		want bool
	}{
		"ex 1": {root: buildTree(11, 1), n: 11, x: 3, want: true},
		"ex 2": {root: buildTree(3, 1), n: 3, x: 1, want: false},
		"ex 3": {root: buildTree(3, 1), n: 3, x: 2, want: true},
	}

	for name, tc := range testdata {
		t.Run(name, func(t *testing.T) {
			got := btreeGameWinningMove(tc.root, tc.n, tc.x)
			diff := cmp.Diff(tc.want, got)
			if diff != "" {
				t.Fatalf(diff)
			}
		})
	}
}
