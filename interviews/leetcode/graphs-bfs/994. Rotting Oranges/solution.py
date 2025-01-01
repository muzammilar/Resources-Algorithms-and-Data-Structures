from collections import deque

ROTTEN = 2
FRESH = 1
EMPTY = 0

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Directions for moving: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 1: Find all rotten oranges and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == ROTTEN:
                    queue.append((i, j))
                elif grid[i][j] == FRESH:
                    fresh_count += 1

        # If there are no fresh oranges, no minutes needed
        if fresh_count == 0:
            return 0

        # Step 2: Perform BFS to rot the fresh oranges
        minutes = -1 # intialize to -1 instead of 0 because adding 1 minute gives current minute
        while queue:

            # Increase minutes before processing one level of BFS
            minutes += 1 # this is the current minute

            # Process all rotten oranges at the current level (minute)
            num_oranges = range(len(queue))
            for _ in num_oranges:
                r, c = queue.popleft()

                # Check all 4 directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == FRESH:
                        grid[nr][nc] = ROTTEN  # Turn fresh orange to rotten
                        fresh_count -= 1
                        queue.append((nr, nc))


        # If there are still fresh oranges, return -1
        return minutes if fresh_count == 0 else -1

# Uncomment the following lines to test the function
# print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,2]]))  # Expected output: 4
# print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # Expected output: -1
