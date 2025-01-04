import itertools

class Solution:

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        numbers = [i for i in range(1,10)]
        # Result list to store the valid combinations
        result = []
        # there's also itertools.combinations_with_replacement(numbers, k)
        for combination in itertools.combinations(numbers, k):
            if sum(combination) == n:
                result.append(list(combination))

        return result

    def combinationSum3WitoutItertools(self, k: int, n: int) -> list[list[int]]:
        # Result list to store the valid combinations
        result = []

        # Helper function for backtracking
        def backtrack(start, current_combination, current_sum):
            # If the combination reaches size k and sum equals n, add it to result
            if len(current_combination) == k and current_sum == n:
                result.append(list(current_combination))
                return
            # If the combination length exceeds k or sum exceeds n, stop exploring
            if len(current_combination) > k or current_sum > n:
                return

            # Try adding the next number to the current combination
            for i in range(start, 10):
                current_combination.append(i)
                backtrack(i + 1, current_combination, current_sum + i)
                current_combination.pop()  # Backtrack

        # Start backtracking from number 1
        backtrack(1, [], 0)
        return result

# Example usage:
# solution = Solution()
# print(solution.combinationSum3(3, 7))
