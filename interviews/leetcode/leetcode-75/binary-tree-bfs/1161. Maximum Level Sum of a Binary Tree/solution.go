package main

import "math"

// TreeNode defines the structure for each node in the binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// maxLevelSum returns the 1-based index of the level with the maximum sum
func maxLevelSum(root *TreeNode) int {
	// If the root is nil, return 0 as there's no level
	if root == nil {
		return 0
	}

	queue := []*TreeNode{root} // Queue for level order traversal (BFS)
	maxSum := math.MinInt      // Start with a very small value
	level := 0                 // Current level
	maxLevel := 0              // Level with the maximum sum

	// Perform level order traversal
	for len(queue) > 0 {
		levelSize := len(queue) // Number of nodes at the current level
		currentSum := 0         // Sum of values at the current level
		level++                 // Move to the next level

		// Traverse all nodes at the current level
		for i := 0; i < levelSize; i++ {
			node := queue[0]
			queue = queue[1:]      // Dequeue the node
			currentSum += node.Val // Add node's value to the sum

			// Enqueue left and right children
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}

		// If the sum at the current level is greater than maxSum, update maxSum and maxLevel
		if currentSum > maxSum {
			maxSum = currentSum
			maxLevel = level
		}
	}

	return maxLevel
}

// Uncomment to test the function
// func main() {
//     root := &TreeNode{Val: 1}
//     root.Left = &TreeNode{Val: 2}
//     root.Right = &TreeNode{Val: 3}
//     root.Left.Left = &TreeNode{Val: 4}
//     root.Left.Right = &TreeNode{Val: 5}
//     root.Right.Right = &TreeNode{Val: 6}
//     fmt.Println(maxLevelSum(root)) // Expected Output: 3
// }
