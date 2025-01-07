package main

import "sort"

// eraseOverlapIntervals returns the minimum number of intervals to remove.
func eraseOverlapIntervals(intervals [][]int) int {
	// Sort intervals by their end time
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][1] < intervals[j][1]
	})

	// Initialize the count of intervals to remove
	count := 0
	// Track the end time of the last added interval
	lastEnd := intervals[0][1]

	// Iterate through the intervals and count the removals
	for i := 1; i < len(intervals); i++ {
		// If the current interval overlaps with the last one, remove it
		if intervals[i][0] < lastEnd {
			count++
		} else {
			// Update the lastEnd to be the end of the current interval
			lastEnd = intervals[i][1]
		}
	}

	return count
}

// Main function (commented out by default)
// func main() {
//     intervals := [][]int{{1, 2}, {2, 3}, {3, 4}, {1, 3}}
//     result := eraseOverlapIntervals(intervals)
//     fmt.Println(result) // Output: 1
// }
