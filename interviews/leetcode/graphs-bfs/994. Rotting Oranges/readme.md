### 994. Rotting Oranges

You are given an `m x n` grid `grid` representing a map where:
- `0` represents an empty cell.
- `1` represents a fresh orange.
- `2` represents a rotten orange.

Each minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten. Return the **minimum number of minutes** that must elapse until no fresh orange can remain.

If **no fresh orange exists** or it is impossible for all the fresh oranges to rot, return `-1`.

##### Example 1:

```plaintext
Input: grid = [[2,1,1],[1,1,0],[0,1,2]]
Output: 4
Explanation: After 4 minutes, all oranges have become rotten.
```

##### Example 2:

```plaintext
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: There is one fresh orange in the bottom-left corner that cannot rot, because the rotten oranges are blocked by walls.
```

##### Example 3:

```plaintext
Input: grid = [[0,2]]
Output: 0
Explanation: Since there is no fresh orange, the answer is 0.
```

##### Constraints:
- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j] is either 0, 1, or 2`.

---

#### Approach

To solve this problem efficiently, we can use **Breadth-First Search (BFS)**. BFS is ideal here because we need to process the oranges layer by layer, where each layer represents a minute of time, and all oranges in the layer become rotten at the same time.

##### Steps:
1. **Initialization**:
   - We need to keep track of all the initial rotten oranges and their positions.
   - Start by adding all the rotten oranges to a queue. Each rotten orange will spread to its neighboring fresh oranges.

2. **BFS**:
   - Process all the rotten oranges level by level (each level represents a minute).
   - For each rotten orange, check its 4 neighbors (up, down, left, right). If the neighbor is a fresh orange, turn it rotten and add it to the queue.
   - Keep track of the minutes (or layers in BFS).

3. **Termination**:
   - If after BFS, any fresh oranges are left, return `-1` because they cannot rot.
   - If no fresh oranges remain, return the time it took to rot all the oranges.

4. **Edge Case**:
   - If there are no fresh oranges initially, the answer is `0` because no time is needed.

#### Time Complexity

- **O(m * n)**: We process each cell at most once, where `m` is the number of rows and `n` is the number of columns.

#### Space Complexity

- **O(m * n)**: We need a queue for BFS, and in the worst case, the queue can store all cells, which is `m * n`.
