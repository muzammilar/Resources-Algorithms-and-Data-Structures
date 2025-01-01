### 2542. Maximum Subsequence Score

You are given two 0-indexed integer arrays `nums1` and `nums2`, both of length `n`, and an integer `k`.

The score of a subsequence of indices `i_1, i_2, ..., i_k` (where `0 <= i_1 < i_2 < ... < i_k < n`) is defined as:

    score = min(nums1[i_1], nums1[i_2], ..., nums1[i_k]) + min(nums2[i_1], nums2[i_2], ..., nums2[i_k])

Return the maximum possible score of a subsequence with at most `k` elements.

**Constraints:**

- 1 <= nums1.length == nums2.length == n <= 1000
- 1 <= nums1[i], nums2[i] <= 1000
- 1 <= k <= n
- The subsequence indices must be strictly increasing (i.e., `i_1 < i_2 < ... < i_k`).

---

#### Approach:

To maximize the score of the subsequence while ensuring that we select at most `k` elements, we can approach the problem in the following steps:

1. **Sorting with Tuple Pairs:**
   Form pairs of corresponding elements from `nums1` and `nums2`. Sort these pairs in descending order based on the values from `nums2`. This prioritizes selecting subsequences with larger values from `nums2`.

2. **Heap Usage:**
   Use a heap (min-heap) to maintain the `nums1` values of the selected subsequence. The heap will allow us to efficiently manage the smallest `nums1` values when we add new elements to the subsequence.

3. **Track Subsequence of Size k:**
   As we iterate over the sorted pairs, we ensure that the size of the subsequence never exceeds `k`. If the heap size exceeds `k`, we remove the smallest `nums1` value (since we are maximizing the score).

4. **Score Calculation:**
   For each possible subsequence (with size ≤ `k`), calculate the score and keep track of the maximum score.

5. **Final Result:**
   After processing all possible subsequences, return the maximum score encountered.

##### Time Complexity:
- Sorting the pairs takes **O(n log n)** time.
- Inserting elements into the heap takes **O(log k)** per operation, and since there are at most `n` operations, this part is **O(n log k)**.
Thus, the overall time complexity is **O(n log n)**.

##### Space Complexity:
- We need extra space for the pairs and the heap. The heap will contain at most `k` elements at any time, so the space complexity is **O(k)**.
Thus, the space complexity is **O(k)**.
