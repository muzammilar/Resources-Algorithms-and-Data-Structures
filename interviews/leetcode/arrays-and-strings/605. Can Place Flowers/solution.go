package main

/*
ChatGPT Solution:

Approach:
Traverse the flowerbed array.
Check if the current position is empty (0) and its neighbors (left and right) are also empty (or out of bounds).
If it satisfies the conditions, plant a flower (set to 1) and reduce the required count n.
If n reaches 0, return true.
If traversal ends and n > 0, return false.
*/

func canPlaceFlowers(flowerbed []int, n int) bool {
	length := len(flowerbed)
	for i := 0; i < length && n > 0; i++ {
		if flowerbed[i] == 0 { // Check if the plot is empty
			// Check neighbors
			emptyLeft := (i == 0 || flowerbed[i-1] == 0)
			emptyRight := (i == length-1 || flowerbed[i+1] == 0)

			if emptyLeft && emptyRight { // Safe to plant a flower
				flowerbed[i] = 1 // Plant the flower
				n--              // Reduce the number of flowers to plant
				i++              // Skip the next spot
			}
		}
	}
	return n == 0 // True if all flowers are planted
}
