package main

// Function to count the number of 1 bits in each number from 0 to n
func countBits(n int) []int {
	dp := make([]int, n+1)

	// Loop through all numbers from 1 to n
	for i := 1; i <= n; i++ {
		// If i is even, dp[i] = dp[i / 2]
		// If i is odd, dp[i] = dp[i / 2] + 1
		dp[i] = dp[i>>1] + (i & 1)
	}

	return dp
}

// Main function (commented out by default)
// func main() {
//     n := 5
//     fmt.Println(countBits(n)) // Output: [0, 1, 1, 2, 1, 2]
// }
