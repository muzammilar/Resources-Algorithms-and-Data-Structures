### 1926. Nearest Exit from Entrance in Maze

You are given an `m x n` matrix `maze` representing the maze, where:
- `1` represents a wall, and `0` represents an open path.
- You are also given the entrance coordinates `entrance = [entrance_row, entrance_col]`, which are guaranteed to be an open path (i.e., `maze[entrance_row][entrance_col] == 0`).

Return the **nearest exit** from the entrance in the maze. The **nearest exit** is the exit that is located on the boundary of the maze. The distance from the entrance to an exit is the number of steps needed to get from the entrance to the exit, where one step consists of moving one cell in one of the four directions: up, down, left, or right.

Return the **number of steps** in the shortest path from the entrance to any exit, or `-1` if no exit exists.

##### Example 1:

```plaintext
Input:
maze = [["+","+","+","+",".",".","+","+"],
        ["+",".",".","+",".",".",".","+"],
        ["+",".","+","+",".",".",".","+"],
        [".",".",".","+",".",".",".","+"],
        ["+",".",".","+",".",".",".","+"],
        ["+",".",".",".",".",".",".","+"],
        ["+",".",".",".",".",".",".","+"],
        ["+",".",".",".",".",".",".","+"],
        ["+","+","+","+","+","+","+"]
]
entrance = [1,4]

Output: 1
```

##### Example 2:

```plaintext
Input:
maze = [["+",".","+"],
        ["+",".","+"],
        ["+",".","+"]
]
entrance = [0,1]

Output: 2
```

##### Constraints:
- `maze.length == m`
- `maze[i].length == n`
- `1 <= m, n <= 100`
- `maze[i][j] is either '.' or '+'`.
- `entrance` is on an open path (i.e., `maze[entrance_row][entrance_col] == '.'`).
- There is at least one exit in the maze.

---

#### Approach

To solve this problem efficiently, we can use **Breadth-First Search (BFS)** since BFS is well-suited for finding the shortest path in an unweighted grid.

1. **Breadth-First Search (BFS)**:
   - Start from the entrance and explore all possible paths in four directions: up, down, left, and right.
   - Mark visited cells to avoid revisiting them.
   - For each valid move, push the current position and the step count into the BFS queue.
   - If we reach any cell on the boundary of the maze (i.e., a cell where either the row or the column is `0` or `m-1` or `n-1`), return the number of steps.
   - If no valid exit is found, return `-1`.

2. **Termination**:
   - If we find an exit during BFS traversal, we return the number of steps.
   - If the queue is exhausted and no exit has been found, we return `-1`.

#### Time Complexity

- **O(m * n)**: In the worst case, BFS will visit every cell in the maze once, where `m` is the number of rows and `n` is the number of columns.

#### Space Complexity

- **O(m * n)**: The space is required for the BFS queue and for the visited cells. In the worst case, all cells may be added to the queue.
