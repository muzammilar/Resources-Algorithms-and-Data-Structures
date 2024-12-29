package main

const (
	Left  = 0
	Right = 1
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var maxLength int

// Function to find the longest ZigZag path
func longestZigZag(root *TreeNode) int {
	maxLength = 0
	// Start DFS from the root node, checking both left (0) and right (1) directions
	dfs(root, Left, 0)  // Start left direction
	dfs(root, Right, 0) // Start right direction
	return maxLength
}

// DFS function to explore the tree and calculate the longest ZigZag path
func dfs(node *TreeNode, direction int, length int) {
	if node == nil {
		return
	}

	// Update the max length found so far
	if length > maxLength {
		maxLength = length
	}

	// If the direction is 0 (left), the next move should be to the right
	if direction == Left {
		dfs(node.Right, Right, length+1) // Right direction
		dfs(node.Left, Left, 1)          // Left direction, starting fresh
	} else {
		dfs(node.Left, Left, length+1) // Left direction
		dfs(node.Right, Right, 1)      // Right direction, starting fresh
	}
}

func main() {
	// The main function is commented by default.
	// Example:
	// root := &TreeNode{Val: 1, Left: &TreeNode{Val: 1}, Right: &TreeNode{Val: 1}}
	// fmt.Println(longestZigZag(root)) // Output: 3
}
