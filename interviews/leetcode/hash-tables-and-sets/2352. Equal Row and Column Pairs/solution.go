func equalPairs(grid [][]int) int {
	n := len(grid)
	count := 0

	// Convert rows to tuples (slice)
	rows := make([][]int, n)
	for i := 0; i < n; i++ {
		rows[i] = make([]int, n)
		copy(rows[i], grid[i])
	}

	// Convert columns to slices
	columns := make([][]int, n)
	for j := 0; j < n; j++ {
		columns[j] = make([]int, n)
		for i := 0; i < n; i++ {
			columns[j][i] = grid[i][j]
		}
	}

	// Compare rows and columns
	for _, row := range rows {
		for _, col := range columns {
			equal := true
			for k := 0; k < n; k++ {
				if row[k] != col[k] {
					equal = false
					break
				}
			}
			if equal {
				count++
			}
		}
	}

	return count
}

/*
func main() {
    grid := [][]int{
        {3, 2, 1},
        {1, 2, 3},
        {3, 2, 1},
    }
    fmt.Println(equalPairs(grid))  // Output: 2
}
*/
