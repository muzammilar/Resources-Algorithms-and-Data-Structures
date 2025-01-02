### 162. Find Peak Element

A peak element in an array is an element that is strictly greater than its neighbors. Given an integer array `nums`, you need to find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may assume that `nums[-1] = nums[n] = -∞` (i.e., elements outside the bounds of the array are negative infinity).

### Example 1:
```plaintext
Input: nums = [1, 2, 3, 1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

---

#### Approach

The solution to this problem uses the **binary search** technique. Here’s a breakdown of the approach:

1. **Binary Search**:
   - We divide the array into two halves and check the middle element.
   - If the middle element is greater than its right neighbor, the peak might be in the left half (including the middle element).
   - If the middle element is smaller than its right neighbor, the peak must be in the right half.
   - We continue the binary search until we narrow down to a single peak element.

2. **Why Binary Search?**:
   - The key observation is that we are guaranteed to always have a peak element (because the first and last elements are treated as -∞), so binary search is an optimal approach.
   - By continuously halving the search space, we can find a peak element in **O(log n)** time.

#### Time Complexity

- **Time Complexity**: **O(log n)**
  The algorithm performs a binary search, halving the array at each step, resulting in a logarithmic time complexity.

#### Space Complexity

- **Space Complexity**: **O(1)**
  The algorithm uses a constant amount of space for the variables (`left`, `right`, `mid`).
