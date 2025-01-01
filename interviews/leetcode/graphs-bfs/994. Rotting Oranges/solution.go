package main

func orangesRotting(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	queue := [][]int{}
	freshCount := 0

	// Directions for moving: up, down, left, right
	directions := []struct{ row, col int }{
		{-1, 0}, {1, 0}, {0, -1}, {0, 1},
	}

	// Step 1: Find all rotten oranges and count fresh ones
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 2 {
				queue = append(queue, []int{i, j})
			} else if grid[i][j] == 1 {
				freshCount++
			}
		}
	}

	// If no fresh oranges, return 0
	if freshCount == 0 {
		return 0
	}

	// Step 2: Perform BFS to rot the fresh oranges
	minutes := 0
	for len(queue) > 0 {
		// Process all rotten oranges at the current level (minute)
		levelSize := len(queue)
		for i := 0; i < levelSize; i++ {
			r, c := queue[0][0], queue[0][1]
			queue = queue[1:]

			// Check all 4 directions
			for _, dir := range directions {
				nr, nc := r+dir.row, c+dir.col
				if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1 {
					grid[nr][nc] = 2 // Turn fresh orange to rotten
					freshCount--
					queue = append(queue, []int{nr, nc})
				}
			}
		}

		// Increase minutes after processing one level of BFS
		minutes++
	}

	// If there are still fresh oranges, return -1
	if freshCount > 0 {
		return -1
	}
	return minutes
}

// Uncomment the following lines to test the function
// fmt.Println(orangesRotting([][]int{{2,1,1},{1,1,0},{0,1,2}}))  // Expected output: 4
// fmt.Println(orangesRotting([][]int{{2,1,1},{0,1,1},{1,0,1}}))  // Expected output: -1
