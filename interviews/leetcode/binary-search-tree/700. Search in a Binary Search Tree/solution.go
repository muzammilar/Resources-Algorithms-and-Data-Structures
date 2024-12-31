package main

// TreeNode defines the structure for each node in the binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// searchBST searches for a node with the given value in the BST
func searchBST(root *TreeNode, val int) *TreeNode {
	// If the root is nil or the root's value matches the target value, return the root
	if root == nil || root.Val == val {
		return root
	}

	// If the value is smaller, search the left subtree
	if val < root.Val {
		return searchBST(root.Left, val)
	}

	// If the value is greater, search the right subtree
	return searchBST(root.Right, val)
}

// Uncomment to test the function
// func main() {
//     root := &TreeNode{Val: 4}
//     root.Left = &TreeNode{Val: 2}
//     root.Right = &TreeNode{Val: 7}
//     root.Left.Left = &TreeNode{Val: 1}
//     root.Left.Right = &TreeNode{Val: 3}
//     result := searchBST(root, 2)
//     fmt.Println(result.Val)  // Expected Output: 2
// }
