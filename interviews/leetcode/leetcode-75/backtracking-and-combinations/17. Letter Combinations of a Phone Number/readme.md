### 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below:

2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"

Note:
- The input string will only contain digits in the range from 2 to 9.
- The answer should not contain duplicate combinations.

---

#### Approach

1. Backtracking Approach:
   - We treat this problem as one of generating all possible combinations of letters.
   - Each digit corresponds to a group of letters. We will explore each group for every digit, combining them as we move along the string.
   - We need to generate all combinations by taking one letter from each corresponding set of letters for each digit.
   - This will be done using a backtracking technique, which will build combinations as we go through each digit.

2. Backtracking Explanation:
   - For each digit, recursively add all its possible corresponding letters to the current combination.
   - Once we’ve built a combination of length equal to the number of digits, we store the combination.
   - Continue this process for each digit in the input string.

#### Time

The time complexity is O(4^n), where `n` is the length of the input string. This is because each digit could correspond to up to 4 letters (for digits '7' and '9'), and we explore all combinations.


#### Space

The space complexity is also O(4^n), as the result list stores all combinations, and each combination has a length of `n`.
