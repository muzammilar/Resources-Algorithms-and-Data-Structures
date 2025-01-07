package main

import "sort"

// findMinArrowShots returns the minimum number of arrows to burst all balloons.
func findMinArrowShots(intervals [][]int) int {
	// Sort intervals by their end time
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})

	// Initialize the number of arrows
	arrows := 1
	// Track the end time of the last balloon that has been burst
	lastEnd := intervals[0][1]

	// Iterate through the intervals and count the number of arrows needed
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] > lastEnd {
			// If the current balloon doesn't overlap, a new arrow is needed
			arrows++
			lastEnd = intervals[i][1]
		}
	}

	return arrows
}

// Main function (commented out by default)
// func main() {
//     intervals := [][]int{{10, 16}, {2, 8}, {1, 6}, {7, 12}}
//     result := findMinArrowShots(intervals)
//     fmt.Println(result) // Output: 2
// }
