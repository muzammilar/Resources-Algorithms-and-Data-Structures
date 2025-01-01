package main

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)      // Number of cities
	visited := make([]bool, n) // To track if a city has been visited

	// Helper function to perform DFS and mark connected cities as visited
	var dfs func(city int)
	dfs = func(city int) {
		for neighbor := 0; neighbor < n; neighbor++ {
			if isConnected[city][neighbor] == 1 && !visited[neighbor] { // Check for direct connection
				visited[neighbor] = true // Mark the neighbor city as visited
				dfs(neighbor)            // Recursively visit all the connected cities
			}
		}
	}

	provinces := 0 // Count of provinces

	// Iterate through each city
	for city := 0; city < n; city++ {
		if !visited[city] { // If the city is unvisited
			visited[city] = true // Mark the current city as visited
			dfs(city)            // Perform DFS to mark all cities connected to the current city
			provinces++          // Increment province count
		}
	}

	// Return the total number of provinces
	return provinces
}

// Uncomment the following line to test the function
// fmt.Println(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))  // Expected output: 2
