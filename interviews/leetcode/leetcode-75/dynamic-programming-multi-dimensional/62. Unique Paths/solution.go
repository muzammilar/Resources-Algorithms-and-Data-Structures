package main

// Function to calculate the number of unique paths to the bottom-right corner
func uniquePaths(m int, n int) int {
	// Create a 1D array to store the results for the current row
	dp := make([]int, n)
	dp[0] = 1 // There is 1 way to reach the first cell (0,0)

	for i := 0; i < m; i++ {
		for j := 1; j < n; j++ {
			dp[j] += dp[j-1] // dp[j] is the sum of the number of ways to move from the left and from above
		}
	}

	return dp[n-1] // The answer is the number of ways to reach the bottom-right corner
}

// Main function (commented out by default)
// func main() {
//     m, n := 3, 7
//     fmt.Println(uniquePaths(m, n)) // Output: 28
// }
