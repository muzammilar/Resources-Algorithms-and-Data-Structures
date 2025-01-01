package main

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected) // Number of cities

	// Parent array to track the root of each city
	parent := make([]int, n)
	for i := range parent {
		parent[i] = i
	}

	// Rank array to keep tree flat (optional)
	rank := make([]int, n)
	for i := range rank {
		rank[i] = 1
	}

	// Find operation with path compression
	var find func(x int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x]) // Path compression
		}
		return parent[x]
	}

	// Union operation with union by rank
	var union func(x, y int)
	union = func(x, y int) {
		rootX := find(x)
		rootY := find(y)
		if rootX != rootY {
			if rank[rootX] > rank[rootY] {
				parent[rootY] = rootX
			} else if rank[rootX] < rank[rootY] {
				parent[rootX] = rootY
			} else {
				parent[rootY] = rootX
				rank[rootX]++ // Increase rank if both roots are the same
			}
		}
	}

	// Union cities that are directly connected
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if isConnected[i][j] == 1 {
				union(i, j)
			}
		}
	}

	// Count the number of provinces by counting unique roots
	provinces := 0
	for i := 0; i < n; i++ {
		if find(i) == i { // Each root represents a province
			provinces++
		}
	}

	return provinces
}

// Uncomment the following line to test the function
// fmt.Println(findCircleNum([][]int{{1,1,0},{1,1,0},{0,0,1}}))  // Expected output: 2
