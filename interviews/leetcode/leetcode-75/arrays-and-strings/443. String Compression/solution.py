class Solution:
    def compress(self, chars: list[str]) -> int:
        write_index = 0  # Position to write compressed characters
        read_index = 0   # Pointer to traverse the array
        n = len(chars)

        while read_index < n:
            current_char = chars[read_index]
            count = 0

            # Count consecutive repeating characters
            while read_index < n and chars[read_index] == current_char:
                read_index += 1
                count += 1

            # Write the character
            chars[write_index] = current_char
            write_index += 1

            # Write the count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        # Return the length of the compressed string
        return write_index
