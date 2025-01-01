package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	// Base case: If the root is nil, the depth is 0
	if root == nil {
		return 0
	}

	// Recursively find the max depth of the left and right subtrees
	leftDepth := maxDepth(root.Left)
	rightDepth := maxDepth(root.Right)

	// Return the maximum of left and right depths, plus 1 for the current node
	if leftDepth > rightDepth {
		return leftDepth + 1
	}
	return rightDepth + 1
}

func maxDepthIterativeApproach(root *TreeNode) int {
	// Base case: if the tree is empty
	if root == nil {
		return 0
	}

	// Initialize a queue for level order traversal
	queue := []*TreeNode{root}
	depth := 0

	// Perform level order traversal
	for len(queue) > 0 {
		// Get the number of nodes at the current level
		levelSize := len(queue)

		// Process all nodes at this level
		for i := 0; i < levelSize; i++ {
			node := queue[0]
			queue = queue[1:]

			// Add left and right children to the queue if they exist
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}

		// Increment depth after processing the current level
		depth++
	}

	return depth
}

// Helper function to create a binary tree from a slice (for testing purposes)
func createBinaryTree(lst []interface{}) *TreeNode {
	if len(lst) == 0 || lst[0] == nil {
		return nil
	}
	root := &TreeNode{Val: lst[0].(int)}
	queue := []*TreeNode{root}
	i := 1
	for i < len(lst) {
		node := queue[0]
		queue = queue[1:]
		if lst[i] != nil {
			node.Left = &TreeNode{Val: lst[i].(int)}
			queue = append(queue, node.Left)
		}
		i++
		if i < len(lst) && lst[i] != nil {
			node.Right = &TreeNode{Val: lst[i].(int)}
			queue = append(queue, node.Right)
		}
		i++
	}
	return root
}

// Uncomment this block to run the test
/*
func main() {
    // Test the solution
    root := createBinaryTree([]interface{}{3, 9, 20, nil, nil, 15, 7})
    result := maxDepth(root)
    fmt.Println(result)  // Output: 3
}
*/
