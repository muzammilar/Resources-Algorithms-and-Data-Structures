func reverseWords(s string) string {
	// Step 1: Trim leading and trailing spaces, then split by whitespace
	words := strings.Fields(s)

	// Step 2: Reverse the list of words
	left, right := 0, len(words)-1
	for left < right {
		// Swap words[left] and words[right]
		words[left], words[right] = words[right], words[left]
		left++
		right--
	}

	// Step 3: Join words with a single space
	return strings.Join(words, " ")
}
