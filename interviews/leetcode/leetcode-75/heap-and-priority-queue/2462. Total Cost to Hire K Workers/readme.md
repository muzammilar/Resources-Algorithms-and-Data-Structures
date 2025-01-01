### 2462. Total Cost to Hire K Workers

## Problem Statement: Total Cost to Hire K Workers

You are given an integer array `costs` where `costs[i]` is the cost of hiring the `i-th` worker. You are also given an integer `k` and an integer `candidates`, which is the number of workers you can consider for hiring from either end of the array. Specifically, you can choose at most `candidates` workers from the front and at most `candidates` workers from the back.

Return the total cost to hire exactly `k` workers. The answer is guaranteed to be less than or equal to `2 * 10^9`.

### Constraints:
- 1 <= costs.length <= 1000
- 1 <= costs[i] <= 1000
- 1 <= k <= costs.length
- 1 <= candidates <= costs.length

```

##### Constraints:
- `1 <= k <= n <= 10^5`
- `1 <= costs[i], workers[i] <= 10^6`

---

## Approach:

We use a greedy approach with priority queues (min-heaps) to efficiently select the workers with the smallest costs from the front and back of the list of candidates:

1. **Heaps for Managing Workers:**
   - A min-heap is used to manage the workers with the smallest costs available from either end of the `costs` array.
   - At any point, we pick the worker with the smallest cost from either end of the `costs` array until we select `k` workers.

2. **Step-by-Step Selection:**
   - First, we populate the min-heap with the workers from the front and back based on the `candidates` value.
   - Then, we extract the worker with the smallest cost, adjust the boundaries for the next worker from the front or back, and add it to the heap.

3. **Termination:**
   - We stop once exactly `k` workers are selected, and their total cost is returned.

### Time Complexity:
- **Heap Operations:**
   - Constructing the initial heap takes **O(n log n)** time.
   - Each insertion and removal from the heap takes **O(log k)**, and since we perform these operations `k` times, the total complexity is **O(k log k)**.
- Thus, the overall time complexity is **O(n log n)**.

### Space Complexity:
- **Heaps:**
   - The space complexity is determined by the space needed for the heap, which stores up to `candidates` workers.
- Thus, the space complexity is **O(candidates)**.
