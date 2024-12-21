class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert the string into a list to modify characters easily
        s = list(s)

        # Define a set of vowels (both uppercase and lowercase)
        vowels = set("aeiouAEIOU")

        # Initialize two pointers
        left, right = 0, len(s) - 1

        # Process until the pointers cross
        while left < right:
            # Move left pointer until a vowel is found
            while left < right and s[left] not in vowels:
                left += 1
            # Move right pointer until a vowel is found
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap the vowels
            s[left], s[right] = s[right], s[left]

            # Move both pointers
            left += 1
            right -= 1

        # Convert the list back to a string and return
        return "".join(s)
