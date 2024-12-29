package main

import "fmt"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func goodNodes(root *TreeNode) int {
	if root == nil {
		return 0
	}

	// Stack to store nodes and the max value encountered on the path
	stack := []struct {
		node   *TreeNode
		maxVal int
	}{
		{root, root.Val},
	}

	count := 0
	for len(stack) > 0 {
		current := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		node, maxVal := current.node, current.maxVal

		// If the current node is a good node, increment the count
		if node.Val >= maxVal {
			count++
		}

		// Update the max value and add children to the stack
		if node.Left != nil {
			stack = append(stack, struct {
				node   *TreeNode
				maxVal int
			}{node.Left, max(maxVal, node.Val)})
		}
		if node.Right != nil {
			stack = append(stack, struct {
				node   *TreeNode
				maxVal int
			}{node.Right, max(maxVal, node.Val)})
		}
	}

	return count
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
