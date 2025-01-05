class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases for n = 0, 1, and 2
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        # Initialize the first three Tribonacci numbers
        t0, t1, t2 = 0, 1, 1
        t_next = 0

        # Calculate the Tribonacci number for n >= 3
        for i in range(3, n + 1):
            # The next Tribonacci number is the sum of the previous three
            t_next = t0 + t1 + t2
            # Update the previous three numbers
            t0, t1, t2 = t1, t2, t_next

        return t_next

# Main function to test
# Uncomment the following lines to test the code:
# solution = Solution()
# print(solution.tribonacci(4))  # Example input
