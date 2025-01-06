package main

// Function to calculate the minimum edit distance
func minDistance(word1 string, word2 string) int {
	m, n := len(word1), len(word2)

	// Use two 1D arrays for space optimization
	dpPrev := make([]int, n+1)
	dpCurr := make([]int, n+1)

	// Initialize the base cases
	for j := 0; j <= n; j++ {
		dpPrev[j] = j
	}

	// Fill the dp table
	for i := 1; i <= m; i++ {
		dpCurr[0] = i // base case for dp[i][0]
		for j := 1; j <= n; j++ {
			if word1[i-1] == word2[j-1] {
				dpCurr[j] = dpPrev[j-1] // no operation needed
			} else {
				dpCurr[j] = min(dpPrev[j-1], min(dpPrev[j], dpCurr[j-1])) + 1
			}
		}
		// Swap the current and previous rows
		dpPrev, dpCurr = dpCurr, dpPrev
	}

	return dpPrev[n]
}

// Helper function to get the minimum of two numbers
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// Main function (commented out by default)
// func main() {
//     word1 := "horse"
//     word2 := "ros"
//     fmt.Println(minDistance(word1, word2)) // Output: 3
// }
