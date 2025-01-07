package main

import (
	"sort"
)

func suggestedProducts(products []string, searchWord string) [][]string {
	// Sort the products lexicographically
	sort.Strings(products)

	var result [][]string
	prefix := ""

	// Iterate through each character of searchWord
	for i := 0; i < len(searchWord); i++ {
		prefix += string(searchWord[i])
		var suggestions []string

		// Find the products that match the current prefix
		for _, product := range products {
			if len(product) >= i+1 && product[:i+1] == prefix {
				suggestions = append(suggestions, product)
			}
		}

		// Store up to 3 suggestions for the current prefix
		if len(suggestions) > 3 {
			suggestions = suggestions[:3]
		}
		result = append(result, suggestions)
	}
	return result
}

// Main function (commented out by default)
// func main() {
//     products := []string{"mobile","mouse","moneypot","monitor","mousepad"}
//     searchWord := "mouse"
//     result := suggestedProducts(products, searchWord)
//     fmt.Println(result)
// }
