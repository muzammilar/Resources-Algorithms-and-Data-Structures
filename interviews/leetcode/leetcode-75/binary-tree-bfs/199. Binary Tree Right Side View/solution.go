package main

// TreeNode defines the structure for each node in the binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// rightSideView returns the right side view of the binary tree
func rightSideView(root *TreeNode) []int {
	// If the root is nil, return an empty slice
	if root == nil {
		return []int{}
	}

	result := []int{}
	queue := []*TreeNode{root} // Queue for level order traversal

	for len(queue) > 0 {
		levelLength := len(queue)

		// Traverse all nodes at the current level
		for i := 0; i < levelLength; i++ {
			node := queue[0]
			queue = queue[1:] // Dequeue the node

			// If this is the rightmost node at the current level, add it to the result
			if i == levelLength-1 {
				result = append(result, node.Val)
			}

			// Enqueue left and right children
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
	}

	return result
}

// Uncomment to test the function
// func main() {
//     root := &TreeNode{Val: 1}
//     root.Left = &TreeNode{Val: 2}
//     root.Right = &TreeNode{Val: 3}
//     root.Left.Right = &TreeNode{Val: 5}
//     root.Right.Right = &TreeNode{Val: 4}
//     fmt.Println(rightSideView(root)) // Expected Output: [1, 3, 4]
// }
