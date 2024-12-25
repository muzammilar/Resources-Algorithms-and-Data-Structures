class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        # Iterate through each character in the string
        for ch in s:
            if ch == '*':
                # If character is '*', pop the last character from the stack
                stack.pop()
            else:
                # If character is not '*', add it to the stack
                stack.append(ch)

        # Convert the stack back to a string and return it
        return ''.join(stack)

# Example usage
# print(remove_stars("ab*c*d*ef"))  # Output: "ef"
# print(remove_stars("****"))       # Output: ""
# print(remove_stars("abc*def**"))  # Output: "ad"
