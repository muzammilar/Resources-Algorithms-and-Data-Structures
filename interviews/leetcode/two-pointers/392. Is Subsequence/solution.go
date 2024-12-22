
func isSubsequence(s string, t string) bool {
	i, j := 0, 0

	for i < len(s) && j < len(t) {
		if s[i] == t[j] {
			i++ // Move pointer in s if characters match
		}
		j++ // Always move pointer in t
	}

	return i == len(s) // Check if we matched all characters in s
}

/*
func main() {
    // Test cases
    fmt.Println(isSubsequence("abc", "ahbgdc"))  // Output: true
    fmt.Println(isSubsequence("axc", "ahbgdc"))  // Output: false
    fmt.Println(isSubsequence("", "ahbgdc"))     // Output: true
    fmt.Println(isSubsequence("abc", ""))        // Output: false
}
*/
