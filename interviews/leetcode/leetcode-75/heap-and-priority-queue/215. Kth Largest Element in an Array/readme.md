### 215. Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in **sorted order**, not the `kth` distinct element.

##### Example 1:

```plaintext
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Explanation: The second largest element is 5.
```

##### Example 2:

```plaintext
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

##### Constraints:
- `1 <= k <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`

---

#### Approach - Heap

There are several approaches to solve this problem, but the most efficient method in terms of time complexity for finding the **kth largest element** in an unsorted array is using a **Min-Heap** or **Quickselect**. We'll discuss both approaches.

##### 1. Using a Min-Heap:
- Use a min-heap of size `k` to store the largest `k` elements in the array.
- Iterate through the array and add elements to the heap. If the heap exceeds `k` elements, remove the smallest element (the root of the min-heap).
- After processing all elements, the root of the heap will contain the `kth` largest element.

##### 2. Quickselect Algorithm:
- The quickselect algorithm is an efficient selection algorithm that works by partitioning the array around a pivot.
- The pivot is chosen such that all elements greater than the pivot are on one side, and all elements smaller are on the other.
- This algorithm has an average time complexity of `O(n)` but can be `O(n^2)` in the worst case.

In this solution, we'll implement the **Min-Heap** approach, which is easier to implement and guarantees `O(n log k)` time complexity.

#### Time Complexity

- **O(n log k)**: We iterate through all `n` elements, and for each element, we either insert it into the heap or remove the smallest element, both of which take `O(log k)` time.

#### Space Complexity

- **O(k)**: We use a heap to store at most `k` elements at a time.

---

### Approach - Sorting

##### 1. Sorting Approach:
- **Sort the array in descending order**.
- The `k`th largest element will be at the index `k-1` in the sorted array, as array indices start at `0`.

##### 2. Steps:
1. **Sort** the array in descending order.
2. **Return** the element at index `k-1` as the `k`th largest element.

This approach is easy to implement but may not be the most optimal in terms of time complexity when compared to other methods like using a heap.

#### Time Complexity

- **O(n log n)**: Sorting the array takes `O(n log n)` time, where `n` is the number of elements in the array.

#### Space Complexity

- **O(1)** if we sort in-place, or **O(n)** if we require additional space for sorting.
