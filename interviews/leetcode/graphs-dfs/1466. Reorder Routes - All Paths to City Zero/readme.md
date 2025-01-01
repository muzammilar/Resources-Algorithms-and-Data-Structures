### 1466. Reorder Routes to Make All Paths Lead to the City Zero

You are given a connected, undirected graph with `n` cities numbered from `0` to `n-1`. There are `n-1` roads such that each road connects two cities. Roads are represented as a 2D array `connections` where each element `connections[i] = [ai, bi]` represents a bidirectional road between city `ai` and city `bi`. Some roads need to be reordered to make all paths lead to city `0`.

Return the minimum number of roads that need to be reordered so that all paths lead to city `0`. In other words, you need to reorder the roads such that all roads point towards city `0`.

##### Example 1:

```plaintext
Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: The roads are given as follows:
   0 → 1 → 3 ← 2
   ↓
   4 → 5
We need to reorder the roads:
- [1,3] → reorder to make it 3 → 1
- [2,3] → reorder to make it 3 → 2
- [4,5] → reorder to make it 5 → 4
After reordering, all roads point towards city 0.
```

##### Example 2:

```plaintext
Input: n = 3, connections = [[0,1],[1,2]]
Output: 2
Explanation: The roads are already directed towards city 0, so no reorder is needed.
```

##### Constraints:
- `2 <= n <= 100`
- `n - 1 <= connections.length <= 10^4`
- `connections[i]` is of length 2.
- `0 <= connections[i][0], connections[i][1] < n`
- No duplicate roads exist.

---

#### Approach

The problem can be solved using **Depth First Search (DFS)** or **Breadth First Search (BFS)**. The goal is to traverse the graph and count how many roads need to be reordered. We can use DFS to visit all cities and check the direction of the roads.

1. **Graph Representation**:
   - Represent the graph as an adjacency list where each road between cities is represented by an edge.
   - For each road, if it's not directed towards city `0`, we need to reorder it. We can determine this by checking the direction during DFS traversal.

2. **DFS Traversal**:
   - We will use DFS to traverse from city `0` and check for each edge if it needs to be reordered.
   - If a road leads away from city `0`, it needs to be reordered, so we increment a counter.

3. **Counting Reordered Roads**:
   - Each road that needs to be reordered will increase the reorder count.

#### Time Complexity

- **O(n)**: We traverse each node and edge exactly once in the DFS traversal.

#### Space Complexity

- **O(n)**: We need space to store the adjacency list and the visited cities array.
