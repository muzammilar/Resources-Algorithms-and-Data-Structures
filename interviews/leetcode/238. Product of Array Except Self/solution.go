
func productExceptSelf(nums []int) []int {
	n := len(nums)
	answer := make([]int, n)

	// Step 1: Calculate prefix products
	prefix := 1
	for i := 0; i < n; i++ {
		answer[i] = prefix
		prefix *= nums[i]
	}

	// Step 2: Calculate postfix products and multiply with prefix
	postfix := 1
	for i := n - 1; i >= 0; i-- {
		answer[i] *= postfix
		postfix *= nums[i]
	}

	return answer
}
