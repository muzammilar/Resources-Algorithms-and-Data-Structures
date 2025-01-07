### 739. Daily Temperatures

Given a list of daily temperatures, where temperatures[i] is the temperature of the day `i`, return a list of integers where each integer represents the number of days you have to wait after the current day to get a warmer temperature. If there is no future day for which this is possible, put 0 instead.

- Implement the following method:
  - `dailyTemperatures(temperatures: List[int]) -> List[int]`: Given a list of temperatures, return a list where each element represents the number of days you need to wait for a warmer temperature.

#### Approach:

1. **Use a Stack**: This problem can be efficiently solved using a stack to keep track of indices of the temperatures that have not yet found a warmer day.

2. **Iterate Over the Temperatures**:
   - For each temperature, check if the stack is not empty and the temperature at the current index is greater than the temperature at the top of the stack.
   - If true, it means we have found a warmer temperature, so we can calculate the number of days (current index - index stored at the top of the stack).
   - Push the current index onto the stack if it hasn't found a warmer day yet.

3. **Time Complexity**: Each index is pushed and popped from the stack at most once, so the time complexity is O(n), where `n` is the number of days.

4. **Space Complexity**: The space complexity is O(n) for the stack.
