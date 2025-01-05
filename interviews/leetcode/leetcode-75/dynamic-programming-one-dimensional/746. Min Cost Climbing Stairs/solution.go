package main

func minCostClimbingStairs(cost []int) int {
	// If there are fewer than 2 stairs, return 0 as no cost is needed
	if len(cost) < 2 {
		return 0
	}

	// Initialize the first two steps' costs
	dp0, dp1 := cost[0], cost[1]

	// Calculate minimum cost for each subsequent step
	for i := 2; i < len(cost); i++ {
		currentCost := min(dp0, dp1) + cost[i]
		dp0, dp1 = dp1, currentCost
	}

	// The minimum cost to reach the top is the minimum of the last two steps
	return min(dp0, dp1)
}

func main() {
	// Uncomment the following lines to test the code:
	// fmt.Println(minCostClimbingStairs([]int{10, 15, 20}))  // Example input
}
