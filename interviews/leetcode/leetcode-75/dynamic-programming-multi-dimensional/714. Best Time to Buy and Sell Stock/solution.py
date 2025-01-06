class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        # Initialize the variables for holding stock and not holding stock
        hold, cash = -prices[0], 0

        for i in range(1, len(prices)):
            # Update the state for holding and not holding the stock
            hold = max(hold, cash - prices[i])
            cash = max(cash, hold + prices[i] - fee)

        return cash

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     prices = [1, 3, 2, 8, 4, 9]
#     fee = 2
#     print(solution.maxProfit(prices, fee))  # Output: 8
