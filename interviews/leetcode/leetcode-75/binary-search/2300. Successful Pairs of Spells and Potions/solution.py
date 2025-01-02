from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Calculate the number of successful pairs of spells and potions.
        A pair is successful if spells[i] * potions[j] >= success.
        """

        # Step 1: Sort the potions array for binary search
        potions.sort()

        result = []

        # Step 2: For each spell, use binary search to find the first valid potion
        for spell in spells:
            # Calculate the minimum potion needed
            min_potion = success / spell
            # Find the index of the first valid potion
            index = bisect_left(potions, min_potion)
            # The number of valid potions is the number of potions from index to the end
            result.append(len(potions) - index)

        return result

# Main function (commented out by default)
# if __name__ == "__main__":
#     solution = Solution()
#     spells = [10, 20, 30]
#     potions = [1, 2, 3, 4, 5]
#     success = 50
#     print(solution.successfulPairs(spells, potions, success))  # Expected output: [4, 4, 5]
