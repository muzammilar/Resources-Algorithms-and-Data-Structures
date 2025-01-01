
import math

def gcdOfStrings(str1, str2):
    # If the concatenation of str1 + str2 is not equal to str2 + str1, return ""
    if str1 + str2 != str2 + str1:
        return ""

    # Find the greatest common divisor of the lengths of the strings
    gcd_length = math.gcd(len(str1), len(str2))

    # Return the substring of str1 that represents the greatest common divisor string
    return str1[:gcd_length]
