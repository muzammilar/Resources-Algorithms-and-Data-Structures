package main

func nearestExit(maze [][]byte, entrance []int) int {
	m, n := len(maze), len(maze[0])

	// Directions for moving: up, down, left, right
	directions := []struct{ row, col int }{
		{-1, 0}, {1, 0}, {0, -1}, {0, 1},
	}

	// BFS queue initialized with entrance
	queue := [][]int{{entrance[0], entrance[1], 0}} // (row, col, steps)
	maze[entrance[0]][entrance[1]] = '+'            // Mark entrance as visited

	// BFS to find the nearest exit
	for len(queue) > 0 {
		// Dequeue the first element
		r, c, steps := queue[0][0], queue[0][1], queue[0][2]
		queue = queue[1:]

		// If we reach an exit (boundary cell)
		if (r == 0 || r == m-1 || c == 0 || c == n-1) && (r != entrance[0] || c != entrance[1]) {
			return steps
		}

		// Explore four possible directions
		for _, dir := range directions {
			nr, nc := r+dir.row, c+dir.col
			if nr >= 0 && nr < m && nc >= 0 && nc < n && maze[nr][nc] == '.' {
				maze[nr][nc] = '+' // Mark as visited
				queue = append(queue, []int{nr, nc, steps + 1})
			}
		}
	}
	return -1 // No exit found
}

// Uncomment the following lines to test the function
// fmt.Println(nearestExit([][]string{
//     {"+", "+", "+", "+", ".", ".", "+", "+"},
//     {"+", ".", ".", "+", ".", ".", ".", "+"},
//     {"+", ".", "+", "+", ".", ".", ".", "+"},
//     {".", ".", ".", "+", ".", ".", ".", "+"},
//     {"+", ".", ".", "+", ".", ".", ".", "+"},
//     {"+", ".", ".", ".", ".", ".", ".", "+"},
//     {"+", ".", ".", ".", ".", ".", ".", "+"},
//     {"+", ".", ".", ".", ".", ".", ".", "+"},
//     {"+", "+", "+", "+", "+", "+", "+"}
// }, []int{1, 4}))  // Expected output: 1
