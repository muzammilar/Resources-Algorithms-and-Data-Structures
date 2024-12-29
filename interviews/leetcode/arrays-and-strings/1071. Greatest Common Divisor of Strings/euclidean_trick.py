import math
class Solution:
    # The trick is to first find the GCD of the two strings and
    # only use that length
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # compute lengths
        l1 = len(str1)
        l2 = len(str2)

        # find the gcd of the lengths
        #gcd = math.gcd(l1, l2)
        gcd = self.gcd(l1, l2)

        # verify that both strings are repeated patterns
        pattern = str1[:gcd]
        pat2 = str2[:gcd]

        # both patterns must be same
        if pat2!=pattern:
            return ""

        # verify the strings only have one pattern
        for i in range(l1//gcd):
            if pattern!=str1[i*gcd:(i+1)*gcd]:
                return ""

        for i in range(l2//gcd):
            if pattern!=str2[i*gcd:(i+1)*gcd]:
                return ""

        return pattern

    def gcd(self, a: int, b:int):
        while b != 0:
            a, b = b, a%b
        return a

    def gcd_recursive(self, a, b):
        if(b == 0):
            return a
        return self.gcd_recursive(b, a % b)
