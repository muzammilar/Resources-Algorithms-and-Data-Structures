package main

// Function to calculate the maximum profit with a transaction fee
func maxProfit(prices []int, fee int) int {
	hold, cash := -prices[0], 0

	for i := 1; i < len(prices); i++ {
		// Update hold and cash for each day
		hold = max(hold, cash-prices[i])
		cash = max(cash, hold+prices[i]-fee)
	}

	return cash
}

// Main function (commented out by default)
// func main() {
//     prices := []int{1, 3, 2, 8, 4, 9}
//     fee := 2
//     fmt.Println(maxProfit(prices, fee)) // Output: 8
// }
