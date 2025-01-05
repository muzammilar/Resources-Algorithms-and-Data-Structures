package main

import "math"

var MOD = getMod()

func getMod() int {
	return int(math.Pow(10, 9) + 7)
}

// Function to calculate the number of ways to tile a 2 x n board
func numTilings(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}

	dp := make([]int, n+1)
	dp[0], dp[1], dp[2] = 1, 1, 2

	for i := 3; i <= n; i++ {
		dp[i] = (dp[i-1] + dp[i-2] + 2*dp[i-3]) % MOD
	}

	return dp[n]
}

// Main function (commented out by default)
// func main() {
//     n := 3
//     fmt.Println(numTilings(n)) // Output: 5
// }
