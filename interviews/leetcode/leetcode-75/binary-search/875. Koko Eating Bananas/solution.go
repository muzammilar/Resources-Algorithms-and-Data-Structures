package main

import (
	"math"
	"slices"
)

// Helper function to calculate the total hours needed at speed k
func hoursNeeded(piles []int, k int) int {
	totalHours := 0
	for _, pile := range piles {
		totalHours += int(math.Ceil(float64(pile) / float64(k)))
	}
	return totalHours
}

// Function to find the minimum eating speed k
func minEatingSpeed(piles []int, h int) int {
	left, right := 1, slices.Max(piles)

	// Binary search for the minimum speed k
	for left < right {
		mid := (left + right) / 2
		if hoursNeeded(piles, mid) <= h {
			right = mid
		} else {
			left = mid + 1
		}
	}

	return left
}

func main() {
	// Main function (commented out by default)
	// piles := []int{3, 6, 7, 11}
	// h := 8
	// fmt.Println(minEatingSpeed(piles, h))  // Expected output: 4
}
