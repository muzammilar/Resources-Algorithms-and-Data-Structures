class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # If there are fewer than 2 stairs, return 0 as no cost is needed
        if len(cost) < 2:
            return 0

        # Initialize the first two steps' costs
        dp0, dp1 = cost[0], cost[1]

        # Calculate minimum cost for each subsequent step
        for i in range(2, len(cost)):
            # Calculate the cost for the current step
            current_cost = min(dp0, dp1) + cost[i]
            # Update the previous two steps
            dp0, dp1 = dp1, current_cost

        # The minimum cost to reach the top is the minimum of the last two steps
        return min(dp0, dp1)


# Main function to test
def main():
    solution = Solution()
    print(solution.minCostClimbingStairs([10, 15, 20]))  # Example input

# Uncomment the following line to run the main function:
# main()
