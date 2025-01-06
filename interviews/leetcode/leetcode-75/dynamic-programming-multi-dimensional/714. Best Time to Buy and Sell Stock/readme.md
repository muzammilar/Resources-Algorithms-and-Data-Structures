### 714. Best Time to Buy and Sell Stock with Transaction Fee

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day. You are also given an integer `fee`, which represents a transaction fee for every buy/sell operation.

You need to find the maximum profit you can achieve. You may complete as many transactions as you like, but you must pay the transaction fee each time you buy or sell a stock.

Return the maximum profit you can achieve after performing as many transactions as needed, where the fee is deducted for each sale.

##### Example:

Input:
`prices = [1, 3, 2, 8, 4, 9]`,
`fee = 2`
Output:
`8`
Explanation:
The maximum profit can be achieved by:
- Buying at price `1` and selling at price `8`, profit = `8 - 1 - 2 = 5`
- Buying at price `4` and selling at price `9`, profit = `9 - 4 - 2 = 3`
- Total profit = `5 + 3 = 8`

---

#### Approach:

This problem can be solved using **Dynamic Programming (DP)**.

1. **Define DP State**:
   Let `hold[i]` represent the maximum profit on the `i-th` day when holding a stock.
   Let `cash[i]` represent the maximum profit on the `i-th` day without holding a stock (i.e., the stock is sold).

2. **Base Case**:
   - On day `0`, if we do not hold a stock, the profit is `0` (i.e., `cash[0] = 0`).
   - On day `0`, if we hold a stock, the profit is `-prices[0]` (i.e., `hold[0] = -prices[0]`).

3. **Recurrence Relation**:
   - If we do not hold any stock on day `i`, we either:
     - Stay in the `cash` state: `cash[i] = cash[i-1]`
     - Sell the stock we were holding: `cash[i] = hold[i-1] + prices[i] - fee`
   - If we are holding a stock on day `i`, we either:
     - Stay in the `hold` state: `hold[i] = hold[i-1]`
     - Buy a new stock: `hold[i] = cash[i-1] - prices[i]`

4. **Optimization**:
   - We can reduce the space complexity by using two variables (`hold` and `cash`) instead of two arrays, because we only need the values from the previous day.

---

#### Time Complexity:
- **O(n)**: We only need to iterate through the prices array once.

#### Space Complexity:
- **O(1)**: We use only a constant amount of extra space.
