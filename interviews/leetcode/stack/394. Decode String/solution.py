
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # Stack to help in decoding
        current_num = 0  # To track the multiplier (k)
        current_str = ""  # To track the current string

        for char in s:
            if char.isdigit():
                # Build the multiplier number
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push the current string and number onto the stack
                stack.append((current_str, current_num))
                current_str, current_num = "", 0  # Reset for the next part
            elif char == ']':
                # Pop from the stack and decode
                last_str, num = stack.pop()
                current_str = last_str + current_str * num  # Repeat the string
            else:
                # Accumulate the current string
                current_str += char

        return current_str

# Test the solution
# if __name__ == "__main__":
#     solution = Solution()
#     # Example test case
#     s = "3[a2[c]]"
#     print(solution.decodeString(s))  # Output: "accaccacc"
