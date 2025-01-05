### 1137. N-th Tribonacci Number


The Tribonacci sequence Tn is defined as follows:

- T0 = 0, T1 = 1, T2 = 1
- For n >= 3, Tn = Tn-1 + Tn-2 + Tn-3

Given an integer `n`, return the value of Tn.

#### Approach:

To solve the problem, we need to calculate the N-th Tribonacci number. We can use an iterative approach to generate the sequence.

1. We first initialize the first three Tribonacci numbers as `0`, `1`, and `1`.
2. Then, for each number starting from the fourth, we calculate the value as the sum of the previous three numbers.
3. We continue this process until we reach the N-th number.
4. The result will be stored in the last number of the sequence.

The iterative approach ensures that we only need to calculate each number once, leading to an efficient solution.

#### Time Complexity:
- The time complexity is **O(n)** because we compute each Tribonacci number once.

#### Space Complexity:
- The space complexity is **O(1)** as we only need to store three variables to hold the last three values.
