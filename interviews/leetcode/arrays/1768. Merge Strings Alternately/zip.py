class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # use zip to combine them both
        out = []
        for i , j in zip(word1,word2):
            out.extend([i, j])

        # append remaining words
        out.append(word1[len(word2):])
        out.append(word2[len(word1):])

        return "".join(out)
