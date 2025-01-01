package main

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	// Graph represented by an adjacency list
	graph := make(map[string][][]interface{})

	// Build the graph with equations and values
	for i, eq := range equations {
		u, v := eq[0], eq[1]
		graph[u] = append(graph[u], []interface{}{v, values[i]})
		graph[v] = append(graph[v], []interface{}{u, 1 / values[i]})
	}

	// Helper function for DFS
	var dfs func(start, end string, visited map[string]bool) float64
	dfs = func(start, end string, visited map[string]bool) float64 {
		if start == end {
			return 1.0
		}
		visited[start] = true
		for _, neighbor := range graph[start] {
			neighborNode := neighbor[0].(string)
			weight := neighbor[1].(float64)
			if !visited[neighborNode] {
				result := dfs(neighborNode, end, visited)
				if result != -1.0 {
					return result * weight
				}
			}
		}
		return -1.0
	}

	// Answer the queries
	var result []float64
	for _, query := range queries {
		u, v := query[0], query[1]
		_, existsV := graph[v]
		_, existsU := graph[u]
		if !existsU || !existsV {
			result = append(result, -1.0)
		} else {
			result = append(result, dfs(u, v, make(map[string]bool)))
		}
	}

	return result
}

// Uncomment the following line to test the function
// fmt.Println(calcEquation([][]string{{"a", "b"}, {"b", "c"}}, []float64{2.0, 3.0}, [][]string{{"a", "c"}, {"b", "a"}, {"a", "e"}, {"a", "a"}, {"x", "x"}}))  // Expected output: [6.0, 0.5, -1.0, 1.0, -1.0]
