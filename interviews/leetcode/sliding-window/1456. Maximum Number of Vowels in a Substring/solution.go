package main

func maxVowels(s string, k int) int {
	vowels := map[rune]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true}
	maxVowels := 0
	currentVowels := 0

	// Step 1: Count vowels in the first 'k' characters
	for i := 0; i < k; i++ {
		if vowels[rune(s[i])] {
			currentVowels++
		}
	}
	maxVowels = currentVowels

	// Step 2: Use sliding window to check other substrings
	for i := k; i < len(s); i++ {
		if vowels[rune(s[i])] {
			currentVowels++
		}
		if vowels[rune(s[i-k])] {
			currentVowels--
		}
		if currentVowels > maxVowels {
			maxVowels = currentVowels
		}
	}

	return maxVowels
}

/*
func main() {
    s := "abciiidef"
    k := 3
    fmt.Println(maxVowels(s, k)) // Output: 3
}
*/
