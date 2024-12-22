from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Create a frequency counter for the elements in the array
        freq = Counter(nums)
        pairs = 0

        # Iterate through the numbers in the array
        for num in freq:
            complement = k - num

            # If complement exists, form the pair
            if complement in freq:
                if num == complement:  # Special case when both numbers are the same
                    pairs += freq[num] // 2
                else:
                    # The number of pairs is the minimum of the frequency of num and its complement
                    pairs += min(freq[num], freq[complement])
                    # Make sure we don't count the same pair again
                    freq[num] = 0
                    freq[complement] = 0

        return pairs
