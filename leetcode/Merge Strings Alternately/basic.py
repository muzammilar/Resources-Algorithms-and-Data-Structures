class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # get length of both words
        len1 = len(word1)
        len2 = len(word2)

        # optimization - null strings
        if len1 == 0:
            return word2
        elif len2 == 0:
            return word1

        # compute the difference and similarity in length of both
        diff = abs(len2-len1)
        sim = max(len2,len1) - diff

        # merge similar results
        result = []
        for i in range(sim):
            result.extend([word1[i], word2[i]])

        # add remaining words
        remaining = ""
        if len2>len1:
            remaining = word2[sim:]
        elif len1>len2:
            remaining = word1[sim:]
        result.append(remaining)

        # return results
        return "".join(result)
