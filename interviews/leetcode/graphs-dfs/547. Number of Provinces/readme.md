### 547. Number of Provinces

You are given a 2D matrix `isConnected` where `isConnected[i][j]` is `1` if city `i` and city `j` are directly connected, otherwise `isConnected[i][j]` is `0`. Return the total number of provinces. A province is a group of directly or indirectly connected cities, and no other cities are connected to them.

##### Example 1:
```plaintext
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Explanation:
The cities are connected as follows:
- City 0 and City 1 are connected, so they form a province.
- City 2 is separate and forms its own province.
```

##### Example 2:
```plaintext
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation:
Each city is in its own province.
```

##### Constraints:
- `1 <= n <= 200` (The number of cities).
- `isConnected[i][j]` is `1` or `0`.
- `isConnected[i][i]` is always `1`.

#### Approach - DFS Approach

This problem can be approached as a **Graph Traversal** problem. The cities can be considered as nodes and the connections between them as edges.

1. **Depth First Search (DFS)**: We can use DFS to traverse through the connected cities. For each unvisited city, we start a DFS, marking all the cities in the same province as visited. Each DFS initiation indicates the discovery of a new province.

2. **Breadth First Search (BFS)**: Alternatively, BFS can also be used. You can iterate through all cities and for each unvisited city, perform BFS to mark all cities connected to it as visited.

3. **Union-Find (Disjoint Set Union - DSU)**: We can use Union-Find to efficiently group connected cities. Every time we find a connection between two cities, we union their sets.

#### Time Complexity - DFS Approach

- **DFS/BFS**:
  - **O(n^2)** where `n` is the number of cities. This is because we traverse each city and check connections to every other city.

- **Union-Find**:
  - **O(n + m)**, where `n` is the number of cities and `m` is the number of connections (edges), with almost constant time complexity due to path compression and union by rank.

#### Space Complexity - DFS Approach

- **DFS/BFS**:
  - **O(n)** for storing the visited cities.

- **Union-Find**:
  - **O(n)** for the parent array and possibly for the rank array.

#### Union Find Approach

* Time Complexity: `O(n + m)`, where n is the number of cities and m is the number of edges.
* Space Complexity: `O(n)` for the parent and rank arrays.

* Union-Find efficiently reduces the time complexity compared to DFS/BFS by keeping track of the connected components in almost constant time due to path compression and union by rank.
* The find function uses path compression to ensure that future find operations are faster.
* The union function uses union by rank to attach the smaller tree to the root of the larger tree, keeping the structure balanced and flat.
* Each union operation efficiently connects two cities, and by the end, the number of distinct components (provinces) is determined by counting the unique roots.
