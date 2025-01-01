package main

// TreeNode defines the structure for each node in the binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// deleteNode deletes a node with the given value in the BST and returns the new root
func deleteNode(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return nil
	}

	// If the value is smaller, move to the left subtree
	if val < root.Val {
		root.Left = deleteNode(root.Left, val)
	} else if val > root.Val {
		// If the value is greater, move to the right subtree
		root.Right = deleteNode(root.Right, val)
	} else {
		// If the value is equal to root's value, this is the node to delete
		if root.Left == nil {
			return root.Right
		} else if root.Right == nil {
			return root.Left
		}
		// If the node has two children, find the in-order successor
		successor := findMin(root.Right)
		// Replace root's value with the successor's value
		root.Val = successor.Val
		// Delete the in-order successor
		root.Right = deleteNode(root.Right, successor.Val)
	}

	return root
}

// findMin finds the node with the smallest value in the BST
func findMin(node *TreeNode) *TreeNode {
	for node.Left != nil {
		node = node.Left
	}
	return node
}

// Uncomment to test the function
// func main() {
//     root := &TreeNode{Val: 5}
//     root.Left = &TreeNode{Val: 3}
//     root.Right = &TreeNode{Val: 6}
//     root.Left.Left = &TreeNode{Val: 2}
//     root.Left.Right = &TreeNode{Val: 4}
//     root.Right.Right = &TreeNode{Val: 7}
//     result := deleteNode(root, 3)
//     fmt.Println(result.Val)  // Expected Output: 5 (the new root after deletion)
// }
