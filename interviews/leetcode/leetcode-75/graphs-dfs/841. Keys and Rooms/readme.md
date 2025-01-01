### 841. Keys and Rooms

You are given a list of rooms where each room may contain some keys to other rooms. Initially, you are in room 0, and you have access to all the keys in the rooms you visit. Your goal is to determine if you can visit all the rooms.

Each room is represented by a list of keys. If room `i` contains a key to room `j`, then you can visit room `j`. However, not all rooms may be reachable, and some rooms may contain keys to other rooms.

##### Example 1

```plaintext
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation:
We have 4 rooms, and we start in room 0.
- Room 0 contains a key to room 1.
- Room 1 contains a key to room 2.
- Room 2 contains a key to room 3.
Since we can visit all the rooms, we return true.
```

##### Example 2

```plaintext
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation:
We have 4 rooms, and we start in room 0.
- Room 0 contains a key to room 1 and 3.
- Room 1 contains a key to room 3, 0, and 1.
- Room 2 contains a key to room 3.
But we cannot reach room 2 from room 0, so the answer is false.
```

#### Approach

The problem can be treated as a graph traversal problem where:
- Each room is a node.
- The keys represent directed edges from one room to another.

We can use **Depth First Search (DFS)** or **Breadth First Search (BFS)** to traverse the graph, starting from room 0. As we traverse the rooms, we keep track of the rooms we can visit. If we visit all rooms, we return `true`; otherwise, `false`.

#### Time Complexity

- **O(n + m)** where `n` is the number of rooms and `m` is the total number of keys. This is because we are visiting each room and key exactly once.

#### Space Complexity

- **O(n)** due to the space needed for the visited rooms.
