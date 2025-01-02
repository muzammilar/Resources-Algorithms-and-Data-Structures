package main

// Problem Statement:
// 374. Guess Number Higher or Lower
// You are playing a game with a secret number between 1 and n. You call a guess function to try to guess the number.
// The function returns:
// -1 if the guessed number is lower than the secret number.
// 1 if the guessed number is higher than the secret number.
// 0 if the guessed number is the secret number.
// Return the secret number.

func guessNumber(n int) int {
	low, high := 1, n // Initializing the search range from 1 to n

	for low <= high {
		mid := (low + high) / 2 // Guess the middle number
		result := guess(mid)    // Call the guess API

		if result == 0 { // If the guess is correct, return the number
			return mid
		}
		if result == -1 { // If the guess is too high, move the upper bound down
			high = mid - 1
			continue
		}
		// If the guess is too low, move the lower bound up
		low = mid + 1

	}
	return -1 // Should not reach here
}

// guess is a mock function to simulate the guess API provided by the problem
func guess(num int) int {
	secret := 6 // Let's assume the secret number is 6 for this example

	if num < secret {
		return 1 // Guess is too low
	} else if num > secret {
		return -1 // Guess is too high
	}
	return 0 // Guess is correct
}

func main() {
	// Main function (commented out by default)
	// n := 10
	// fmt.Println(guessNumber(n))  // Expected output depends on the secret number
}
