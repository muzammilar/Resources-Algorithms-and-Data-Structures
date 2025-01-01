package main

import "fmt"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Helper function for DFS traversal
func dfs(node *TreeNode, maxVal int) int {
	if node == nil {
		return 0
	}

	count := 0
	if node.Val >= maxVal {
		count = 1
	}

	// Update the max value and recurse for left and right children
	maxVal = max(maxVal, node.Val)
	count += dfs(node.Left, maxVal)
	count += dfs(node.Right, maxVal)

	return count
}

func goodNodes(root *TreeNode) int {
	return dfs(root, root.Val)
}

// Helper function to create a binary tree from a slice
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

func main() {
	root := createBinaryTree([]interface{}{3, 1, 4, 3, nil, 1, 5})
	result := goodNodes(root)
	fmt.Println(result) // Output: 4
}
