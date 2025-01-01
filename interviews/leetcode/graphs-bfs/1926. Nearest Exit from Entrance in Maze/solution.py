from collections import deque

VISITED = "+"
WALLED = "+"
NOT_VISITED = "."

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m, n = len(maze), len(maze[0])

        # Directions for moving: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS queue initialized with entrance
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        maze[entrance[0]][entrance[1]] = VISITED  # Mark entrance as visited

        # BFS to find the nearest exit
        while queue:
            r, c, steps = queue.popleft()

            # If we reach an exit (boundary cell)
            if (r == 0 or r == m - 1 or c == 0 or c == n - 1) and (r != entrance[0] or c != entrance[1]):
                return steps

            # Explore four possible directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == NOT_VISITED:
                    maze[nr][nc] = VISITED  # Mark as visited
                    queue.append((nr, nc, steps + 1))

        return -1  # No exit found

# Uncomment the following lines to test the function
# print(Solution().nearestExit([["+", "+", "+", "+", ".", ".", "+", "+"],
#                              ["+", ".", ".", "+", ".", ".", ".", "+"],
#                              ["+", ".", "+", "+", ".", ".", ".", "+"],
#                              [".", ".", ".", "+", ".", ".", ".", "+"],
#                              ["+", ".", ".", "+", ".", ".", ".", "+"],
#                              ["+", ".", ".", ".", ".", ".", ".", "+"],
#                              ["+", ".", ".", ".", ".", ".", ".", "+"],
#                              ["+", ".", ".", ".", ".", ".", ".", "+"],
#                              ["+", "+", "+", "+", "+", "+", "+"]
#                              ], [1, 4]))  # Expected output: 1
