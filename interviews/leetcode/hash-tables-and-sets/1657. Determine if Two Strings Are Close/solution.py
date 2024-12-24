
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # Check if both strings have the same length
        if len(word1) != len(word2):
            return False

        # Count the frequency of characters in both strings
        count1 = Counter(word1)
        count2 = Counter(word2)

        # Check if both strings have the same set of characters
        if set(count1.keys()) != set(count2.keys()):
            return False

        # Check if both strings have the same frequency distribution
        if sorted(count1.values()) != sorted(count2.values()):
            return False

        return True
