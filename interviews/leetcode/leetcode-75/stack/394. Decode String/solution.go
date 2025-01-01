package main

import (
	"fmt"
	"strconv"
)

func decodeString(s string) string {
	stack := []string{} // Stack to help in decoding
	currentNum := 0     // To track the multiplier (k)
	currentStr := ""    // To track the current string

	for i := 0; i < len(s); i++ {
		char := s[i]

		if char >= '0' && char <= '9' {
			// Build the multiplier number
			currentNum = currentNum*10 + int(char-'0')
		} else if char == '[' {
			// Push the current string and number onto the stack
			stack = append(stack, currentStr, fmt.Sprintf("%d", currentNum))
			currentStr, currentNum = "", 0 // Reset for the next part
		} else if char == ']' {
			// Pop from the stack and decode
			numStr := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			lastStr := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			// Repeat the current string
			repeated := ""
			for j := 0; j < stringToInt(numStr); j++ {
				repeated += currentStr
			}

			// Concatenate with the previous part
			currentStr = lastStr + repeated
		} else {
			// Accumulate the current string
			currentStr += string(char)
		}
	}

	return currentStr
}

// Helper function to convert string to integer
func stringToInt(s string) int {
	num, _ := strconv.Atoi(s)
	return num
}

// Uncomment to run the solution and test cases
// func main() {
//     // Example test case
//     s := "3[a2[c]]"
//     result := decodeString(s)
//     fmt.Println(result) // Output: "accaccacc"
// }
