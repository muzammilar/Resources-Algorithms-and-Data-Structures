### 374. Guess Number Higher or Lower

You are playing a game with a secret number between 1 and `n`. You call a `guess` function to try to guess the number. The function returns:

- `-1` if the guessed number is lower than the secret number.
- `1` if the guessed number is higher than the secret number.
- `0` if the guessed number is the secret number.

Return the secret number.

---

#### Approach

The solution uses **binary search** to find the secret number. Here's how it works:

1. Initialize the search range between `1` and `n` (inclusive).
2. At each step, guess the middle number `mid` in the current search range.
3. Call the `guess(mid)` function to check the result:
   - If the result is `0`, we've found the secret number, so return `mid`.
   - If the result is `-1`, the guessed number is too high, so move the upper boundary of the search range to `mid - 1`.
   - If the result is `1`, the guessed number is too low, so move the lower boundary of the search range to `mid + 1`.
4. Repeat the process until we find the secret number.

---

#### Complexity

- **Time Complexity**: **O(log n)**
  Since the search space is halved at each step, the time complexity of this solution is logarithmic in terms of the number of possible guesses (`n`).

- **Space Complexity**: **O(1)**
  We only need a constant amount of extra space to store the low, high, and mid pointers. There are no additional data structures used.
