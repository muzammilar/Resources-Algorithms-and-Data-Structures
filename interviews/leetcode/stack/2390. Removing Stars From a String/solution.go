package main

func removeStars(s string) string {
	stack := make([]rune, 0, len(s))

	// Iterate through each character in the string
	for _, ch := range s {
		if ch == '*' {
			// If character is '*', pop the last character from the stack (the closest non-star character)
			stack = stack[:len(stack)-1]
		} else {
			// If character is not '*', push it onto the stack
			stack = append(stack, ch)
		}
	}

	// Convert the stack back to a string and return it
	return string(stack)
}

/*
func main() {
	// Example usage
	fmt.Println(removeStars("ab*c*d*ef")) // Output: "ef"
	fmt.Println(removeStars("****"))      // Output: ""
	fmt.Println(removeStars("abc*def**")) // Output: "ad"
}
*/
