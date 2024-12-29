package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Function to find the lowest common ancestor
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	// Base case: if root is nil or root is either p or q
	if root == nil || root == p || root == q {
		return root
	}

	// Recursively find LCA in left and right subtrees
	left := lowestCommonAncestor(root.Left, p, q)
	right := lowestCommonAncestor(root.Right, p, q)

	// If p and q are found in different subtrees, root is the LCA
	if left != nil && right != nil {
		return root
	}

	// Otherwise, return the non-null child (either left or right)
	if left != nil {
		return left
	}
	return right
}

func main() {
	// Example test case (this will be commented out)
	// root := &TreeNode{Val: 3, Left: &TreeNode{Val: 5}, Right: &TreeNode{Val: 1}}
	// p := root.Left // 5
	// q := root.Right // 1
	// fmt.Println(lowestCommonAncestor(root, p, q)) // Output: 3
}
