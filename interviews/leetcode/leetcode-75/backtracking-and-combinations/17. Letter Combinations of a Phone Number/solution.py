class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Base case: if the digits string is empty, return an empty list.
        if not digits:
            return []

        # Mapping of digits to letters as per the phone number layout.
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        # Result list to store the combinations.
        result = []

        # Backtracking function to build the combinations.
        def backtrack(index, current_combination):
            # If the current combination is of the same length as digits, add to result.
            if index == len(digits):
                result.append(current_combination)
                return

            # Get the letters corresponding to the current digit.
            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                # Recursively build the combination.
                backtrack(index + 1, current_combination + letter)

        # Start the backtracking with the first digit (index 0).
        backtrack(0, "")

        return result

# Example usage:
# solution = Solution()
# print(solution.letterCombinations("23"))
