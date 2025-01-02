package main

import (
	"sort"
)

// Problem Statement:
// 2300. Successful Pairs of Spells and Potions
// You are given two positive integer arrays spells and potions, of lengths n and m respectively.
// You are also given an integer success.
// You need to find the number of successful pairs of spells and potions.
// A pair of spells i and potions j is successful if spells[i] * potions[j] >= success.
// Return an integer array pairs of length n where pairs[i] is the number of successful pairs of spells[i] and each potion.
func successfulPairs(spells []int, potions []int, success int64) []int {
	// Step 1: Sort the potions array for binary search
	sort.Ints(potions)

	// Step 2: Define the result array
	result := make([]int, len(spells))

	// Step 3: For each spell, use binary search to find the first valid potion
	for i, spell := range spells {
		minPotion := success / int64(spell)
		if success%int64(spell) != 0 { // If there's a remainder, increment the minPotion by 1
			minPotion++
		}

		// Use binary search to find the first potion >= minPotion
		left, right := 0, len(potions)
		for left < right {
			mid := (left + right) / 2
			if int64(potions[mid]) >= minPotion {
				right = mid
			} else {
				left = mid + 1
			}
		}

		// The number of valid potions is the length of the potions array from 'left' to the end
		result[i] = len(potions) - left
	}
	return result
}

func main() {
	// Main function (commented out by default)
	// spells := []int{10, 20, 30}
	// potions := []int{1, 2, 3, 4, 5}
	// success := 50
	// fmt.Println(successfulPairs(spells, potions, success))  // Expected output: [4, 4, 5]
}
