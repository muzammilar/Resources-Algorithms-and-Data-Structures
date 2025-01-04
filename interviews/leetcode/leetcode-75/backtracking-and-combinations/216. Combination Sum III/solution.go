package main

// Function to find all combinations
func combinationSum3(k int, n int) [][]int {
	var result [][]int

	// Backtracking helper function
	var backtrack func(start, currentSum int, currentCombination []int)
	backtrack = func(start, currentSum int, currentCombination []int) {
		// If the combination reaches size k and sum equals n, add it to result
		if len(currentCombination) == k && currentSum == n {
			result = append(result, append([]int{}, currentCombination...))
			return
		}
		// If the combination exceeds size k or sum exceeds n, stop exploring
		if len(currentCombination) > k || currentSum > n {
			return
		}

		// Try adding the next number to the current combination
		for i := start; i <= 9; i++ {
			currentCombination = append(currentCombination, i)
			backtrack(i+1, currentSum+i, currentCombination)
			currentCombination = currentCombination[:len(currentCombination)-1] // Backtrack
		}
	}

	// Start backtracking from number 1
	backtrack(1, 0, []int{})
	return result
}

func main() {
	// Example usage:
	// result := combinationSum3(3, 7)
	// fmt.Println(result)
}
