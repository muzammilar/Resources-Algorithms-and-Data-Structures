### 2300. Successful Pairs of Spells and Potions

You are given two positive integer arrays `spells` and `potions`, of lengths `n` and `m` respectively. You are also given an integer `success`.

You need to find the number of successful pairs of spells and potions. A pair of spells `i` and potions `j` is successful if:

- `spells[i] * potions[j] >= success`

Return an integer array `pairs` of length `n` where `pairs[i]` is the number of successful pairs of spells[i] and each potion.

---

#### Approach

The solution utilizes the following steps:

1. **Sort the Potions Array**:
   We start by sorting the `potions` array in ascending order. This allows us to use binary search efficiently to determine how many potions satisfy the condition for each spell.

2. **Binary Search for Each Spell**:
   For each spell, we need to find how many potions satisfy the condition `spell * potion >= success`. We can calculate the minimum potion needed for a spell by dividing `success` by the spell's value.

3. **Counting Successful Potions**:
   Using binary search (`bisect_left` for Python or custom binary search for Go), we find the index of the first potion that satisfies the condition. The number of successful potions for that spell is the number of potions from that index to the end of the array.

4. **Result**:
   The result is an array of the number of successful pairs for each spell.

---

#### Complexity

- **Time Complexity**:
  - Sorting the `potions` array takes **O(m log m)** where `m` is the length of the `potions` array.
  - For each spell, we perform a binary search on the sorted `potions` array, which takes **O(log m)**.
  - Thus, the total time complexity is **O(m log m + n log m)** where `n` is the length of the `spells` array.

- **Space Complexity**:
  - **O(m)** for sorting the `potions` array.
  - **O(n)** for the result array, where `n` is the length of the `spells` array.
