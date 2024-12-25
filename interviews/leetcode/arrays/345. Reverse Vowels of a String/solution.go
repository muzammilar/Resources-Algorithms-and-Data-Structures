package main

import "strings"

func reverseVowels(s string) string {
	// Convert string to a slice for easier manipulation
	str := []rune(s)

	// Function to check if a character is a vowel
	isVowel := func(ch rune) bool {
		return strings.ContainsRune("aeiouAEIOU", ch)
	}

	// Two pointers
	left, right := 0, len(str)-1

	// Process until pointers meet
	for left < right {
		// Move left pointer until we find a vowel
		for left < right && !isVowel(str[left]) {
			left++
		}
		// Move right pointer until we find a vowel
		for left < right && !isVowel(str[right]) {
			right--
		}

		// Swap vowels
		str[left], str[right] = str[right], str[left]
		left++
		right--
	}

	// Return the modified string
	return string(str)
}
