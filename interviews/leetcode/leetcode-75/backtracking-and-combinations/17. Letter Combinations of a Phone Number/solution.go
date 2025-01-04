package main

// Function to generate letter combinations.
func letterCombinations(digits string) []string {
	if len(digits) == 0 {
		return []string{}
	}

	// Mapping of digits to letters
	phoneMap := map[byte]string{
		'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
		'6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz",
	}

	var result []string

	// Backtracking function to explore combinations.
	var backtrack func(index int, currentCombination string)
	backtrack = func(index int, currentCombination string) {
		if index == len(digits) {
			result = append(result, currentCombination)
			return
		}

		currentDigit := digits[index]
		letters := phoneMap[currentDigit]
		for i := 0; i < len(letters); i++ {
			backtrack(index+1, currentCombination+string(letters[i]))
		}
	}

	// Start the backtracking from the first digit (index 0).
	backtrack(0, "")

	return result
}

func main() {
	// Example usage:
	// result := letterCombinations("23")
	// fmt.Println(result)
}
