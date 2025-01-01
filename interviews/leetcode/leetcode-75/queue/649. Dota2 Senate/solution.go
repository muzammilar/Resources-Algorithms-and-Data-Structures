package main

func predictPartyVictory(senate string) string {
	radiant := []int{} // Queue for Radiant senators
	dire := []int{}    // Queue for Dire senators

	// Initialize the queues with the indices of the senators
	for i, s := range senate {
		if s == 'R' {
			radiant = append(radiant, i)
		} else {
			dire = append(dire, i)
		}
	}

	// Process the senators until one faction wins
	for len(radiant) > 0 && len(dire) > 0 {
		r := radiant[0] // Get the front senator from Radiant
		d := dire[0]    // Get the front senator from Dire

		// Remove the first element from both queues
		radiant = radiant[1:]
		dire = dire[1:]

		// The senator with the smaller index gets to ban the other
		if r < d {
			radiant = append(radiant, r+len(senate)) // Reinsert the Radiant senator at the end
		} else {
			dire = append(dire, d+len(senate)) // Reinsert the Dire senator at the end
		}
	}

	// If Radiant still has senators, they win; otherwise, Dire wins
	if len(radiant) > 0 {
		return "Radiant"
	}
	return "Dire"
}

// Uncomment to test
// func main() {
//     fmt.Println(predictPartyVictory("RD"))  // Output: "Radiant"
//     fmt.Println(predictPartyVictory("RDD"))  // Output: "Dire"
// }
