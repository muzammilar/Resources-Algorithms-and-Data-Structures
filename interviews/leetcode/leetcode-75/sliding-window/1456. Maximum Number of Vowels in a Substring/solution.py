class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set("aeiouAEIOU")
        max_vowels = 0
        current_vowels = 0

        # Step 1: Count vowels in the first 'k' characters
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        # Step 2: Use sliding window to check other substrings
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            if s[i - k] in vowels:
                current_vowels -= 1
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels
