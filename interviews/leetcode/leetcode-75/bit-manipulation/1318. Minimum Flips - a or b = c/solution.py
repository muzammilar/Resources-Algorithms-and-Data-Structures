class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):  # Assume 32-bit integers
            aBit = (a >> i) & 1
            bBit = (b >> i) & 1
            cBit = (c >> i) & 1

            if cBit == 0:
                # Both aBit and bBit should be 0
                flips += aBit + bBit
            else:
                # At least one of aBit or bBit should be 1
                if aBit == 0 and bBit == 0:
                    flips += 1

        return flips

# Main function (commented out by default)
# def main():
#     solution = Solution()
#     a, b, c = 2, 6, 5
#     print(solution.minFlips(a, b, c))  # Output: 3
