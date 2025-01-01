package main

func minReorder(n int, connections [][]int) int {
	// Create adjacency list to represent the graph
	graph := make([][][]int, n)

	// Populate the graph with the connections
	for _, conn := range connections {
		u, v := conn[0], conn[1]
		// Add edge u -> v with a flag 1 indicating this road needs to be reordered
		graph[u] = append(graph[u], []int{v, 1})
		// Add edge v -> u with a flag 0 indicating no reordering is needed
		graph[v] = append(graph[v], []int{u, 0})
	}

	// To track if a city has been visited
	visited := make([]bool, n)
	reorderCount := 0

	// Helper function to perform DFS
	var dfs func(city int)
	dfs = func(city int) {
		visited[city] = true // Mark the current city as visited
		for _, neighborInfo := range graph[city] {
			neighbor, needReorder := neighborInfo[0], neighborInfo[1]
			// If the neighbor city has not been visited
			if !visited[neighbor] {
				// If the edge needs to be reordered, increment reorderCount
				if needReorder == 1 {
					reorderCount++
				}
				// Continue DFS with the neighboring city
				dfs(neighbor)
			}
		}
	}

	// Start DFS from city 0
	dfs(0)

	// Return the total number of roads that need to be reordered
	return reorderCount
}

// Uncomment the following line to test the function
// fmt.Println(minReorder(6, [][]int{{0,1},{1,3},{2,3},{4,0},{4,5}}))  // Expected output: 3
