class Solution:
    def reverseWords(self, s: str) -> str:

        # Step 1: Split the string by whitespace and filter out empty words
        words = s.split()

        # Step 2: Reverse the list of words
        words.reverse()

        # Step 3: Join the words with a single space
        return " ".join(words)
