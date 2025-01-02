# Problem Statement:
# 374. Guess Number Higher or Lower
# You are playing a game with a secret number between 1 and n. You call a guess function to try to guess the number.
# The function returns:
# -1 if the guessed number is lower than the secret number.
# 1 if the guessed number is higher than the secret number.
# 0 if the guessed number is the secret number.
# Return the secret number.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Guess the secret number in the range [1, n] using binary search approach.
        """
        low, high = 1, n  # Initializing the search range from 1 to n

        while low <= high:
            mid = (low + high) // 2  # Guess the middle number
            result = guess(mid)  # Call the guess API

            if result == 0:  # If the guess is correct, return the number
                return mid

            if result == -1:  # If the guess is too high, move the upper bound down
                high = mid - 1
                continue

            # If the guess is too low, move the lower bound up
            low = mid + 1

        return -1  # Should not reach here

# Main function (commented out by default)
# if __name__ == "__main__":
#     solution = Solution()
#     n = 10
#     print(solution.guessNumber(n))  # Expected output depends on the secret number
