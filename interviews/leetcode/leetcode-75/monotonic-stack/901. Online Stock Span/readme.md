### 901. Online Stock Span

Design a system that can calculate the "stock span" of a stock's price on a given day. The stock span is defined as the maximum number of consecutive days (starting from the current day) that the price of the stock has been less than or equal to the price on the current day.

- Implement the following method:
  - `StockSpanner`: A class to handle the stock price queries.
    - `next(price: int) -> int`: Given the price of a stock, calculate and return the stock span for the current price.

#### Approach:

1. **Use a Stack**: The stack will help us efficiently track the days' prices. We will maintain the stack to store pairs of price and its span for consecutive days.

2. **For Each Price**:
   - While the stack is not empty and the current price is greater than or equal to the price at the top of the stack, we pop from the stack. This is because the current price is better than all the previous prices in the stack.
   - The span for the current price is then determined as the difference between the current day and the day represented by the top of the stack. If the stack is empty, this means the current price is the highest so far, and its span is the entire range of days up to this point.

3. **Time Complexity**:
   - Every price is pushed and popped from the stack at most once, making the time complexity O(n), where `n` is the number of prices.

4. **Space Complexity**:
   - The space complexity is O(n) due to the stack storing prices and spans.
