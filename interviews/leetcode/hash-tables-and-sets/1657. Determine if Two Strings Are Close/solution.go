
import "sort"

func closeStrings(word1 string, word2 string) bool {
	if len(word1) != len(word2) {
		return false
	}

	// Create frequency maps for both strings
	count1 := make(map[rune]int)
	count2 := make(map[rune]int)

	for _, ch := range word1 {
		count1[ch]++
	}
	for _, ch := range word2 {
		count2[ch]++
	}

	// Check if both strings have the same set of characters
	for ch := range count1 {
		if _, exists := count2[ch]; !exists {
			return false
		}
	}
	for ch := range count2 {
		if _, exists := count1[ch]; !exists {
			return false
		}
	}

	// Compare the frequency distributions
	freq1 := make([]int, 0, len(count1))
	freq2 := make([]int, 0, len(count2))

	for _, val := range count1 {
		freq1 = append(freq1, val)
	}
	for _, val := range count2 {
		freq2 = append(freq2, val)
	}

	// Sort and compare frequencies
	sort.Ints(freq1)
	sort.Ints(freq2)

	for i := 0; i < len(freq1); i++ {
		if freq1[i] != freq2[i] {
			return false
		}
	}

	return true
}

/*
func main() {
    word1 := "abc"
    word2 := "bca"
    fmt.Println(closeStrings(word1, word2))  // Output: true
}
*/
