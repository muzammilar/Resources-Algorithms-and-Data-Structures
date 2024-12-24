class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
        # Step 1: Convert rows to tuples
        rows = [tuple(grid[i]) for i in range(n)]

        # Step 2: Convert columns to tuples
        columns = [tuple(grid[i][j] for i in range(n)) for j in range(n)]

        # Step 3: Count equal pairs of rows and columns
        count = 0
        for row in rows:
            for col in columns:
                if row == col:
                    count += 1

        return count
