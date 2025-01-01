package main

import "fmt"

func canVisitAllRooms(rooms [][]int) bool {
	// A slice to track the visited rooms
	visited := make([]bool, len(rooms))

	// DFS function to explore rooms
	var dfs func(int)
	dfs = func(room int) {
		// Mark the current room as visited
		visited[room] = true
		// Visit all rooms we can reach with the keys from the current room
		for _, key := range rooms[room] {
			if !visited[key] {
				dfs(key)
			}
		}
	}

	// Start DFS from room 0
	dfs(0)

	// Check if all rooms were visited
	for _, v := range visited {
		if !v {
			return false
		}
	}
	return true
}

func main() {
	// Example usage:
	// Test case 1
	rooms := [][]int{{1}, {2}, {3}, {}}
	fmt.Println(canVisitAllRooms(rooms)) // Output: true

	// Test case 2
	rooms2 := [][]int{{1, 3}, {3, 0, 1}, {2}, {0}}
	fmt.Println(canVisitAllRooms(rooms2)) // Output: false
}
