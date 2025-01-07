class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Initialize the result array with zeros
        result = [0] * len(temperatures)
        # Initialize an empty stack to hold indices
        stack = []

        # Iterate through the temperatures
        for i, _ in enumerate(temperatures):
            # While the stack is not empty and the current temperature is greater
            # than the temperature at the index at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Pop the top index and calculate the number of days to wait
                idx = stack.pop()
                result[idx] = i - idx
            # Push the current index onto the stack
            stack.append(i)

        return result

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
#     result = solution.dailyTemperatures(temperatures)
#     print(result)  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
