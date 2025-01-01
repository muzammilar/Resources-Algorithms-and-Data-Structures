package main

import "fmt"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Helper function to collect the leaf nodes of a binary tree
func getLeaves(root *TreeNode) []int {
	var leaves []int
	if root == nil {
		return leaves
	}

	// If the current node is a leaf, add it to the leaves list
	if root.Left == nil && root.Right == nil {
		leaves = append(leaves, root.Val)
	}

	// Recurse for left and right subtrees
	leaves = append(leaves, getLeaves(root.Left)...)
	leaves = append(leaves, getLeaves(root.Right)...)

	return leaves
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	// Get the leaf nodes for both trees
	leaves1 := getLeaves(root1)
	leaves2 := getLeaves(root2)

	// Compare the leaf nodes of both trees
	if len(leaves1) != len(leaves2) {
		return false
	}
	for i := 0; i < len(leaves1); i++ {
		if leaves1[i] != leaves2[i] {
			return false
		}
	}
	return true
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

func main() {
	// Test the solution
	root1 := createBinaryTree([]interface{}{3, 5, 1, 6, 2, 9, 8, nil, nil, 7, 4})
	root2 := createBinaryTree([]interface{}{3, 5, 1, 6, 7, 4, 2, nil, nil, nil, nil, 9, 8})

	result := leafSimilar(root1, root2)
	fmt.Println(result) // Output: true
}
