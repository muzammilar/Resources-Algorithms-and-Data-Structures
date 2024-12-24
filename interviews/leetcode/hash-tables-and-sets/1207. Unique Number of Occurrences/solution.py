from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # Count the frequency of each number in the array
        count = Counter(arr)

        # Check if any frequency is repeated
        frequency_count = count.values()
        return len(frequency_count) == len(set(frequency_count))
