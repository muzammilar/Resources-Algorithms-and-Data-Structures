package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, target int) int {
	prefixSumCount := map[int]int{0: 1} // Initialize with the base case to handle paths starting from the root
	return dfs(root, target, 0, prefixSumCount)
}

func dfs(root *TreeNode, target, currentSum int, prefixSumCount map[int]int) int {
	if root == nil {
		return 0
	}

	// Update the current running sum
	currentSum += root.Val

	// Check if there is a previous prefix sum that gives the desired result
	result := prefixSumCount[currentSum-target]

	// Update the prefix sum count
	prefixSumCount[currentSum]++

	// Recurse for left and right children
	result += dfs(root.Left, target, currentSum, prefixSumCount)
	result += dfs(root.Right, target, currentSum, prefixSumCount)

	// Backtrack: decrease the count of the current sum
	prefixSumCount[currentSum]--

	return result
}

func main() {
	// The main function is commented by default.
	// Example:
	// root := &TreeNode{Val: 10, Left: &TreeNode{Val: 5, Left: &TreeNode{Val: 3}, Right: &TreeNode{Val: 2}}, Right: &TreeNode{Val: -3, Right: &TreeNode{Val: 11}}}
	// target := 8
	// fmt.Println(pathSum(root, target)) // Output: 3
}
