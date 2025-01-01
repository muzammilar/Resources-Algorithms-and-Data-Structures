package main

func uniqueOccurrences(arr []int) bool {
	count := make(map[int]int)

	// Count the frequency of each number in the array
	for _, num := range arr {
		count[num]++
	}

	freqSet := make(map[int]struct{})

	// Check if any frequency is repeated
	for _, freq := range count {
		if _, exists := freqSet[freq]; exists {
			return false
		}
		freqSet[freq] = struct{}{}
	}

	return true
}

/*
func main() {
    arr := []int{1, 2, 2, 1, 1, 3}
    fmt.Println(uniqueOccurrences(arr))  // Output: true
}
*/
