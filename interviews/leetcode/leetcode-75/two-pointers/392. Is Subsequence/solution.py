class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Two pointers for s and t
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move pointer in s if characters match
            j += 1  # Always move pointer in t

        # If all characters in s are matched, return True
        return i == len(s)
