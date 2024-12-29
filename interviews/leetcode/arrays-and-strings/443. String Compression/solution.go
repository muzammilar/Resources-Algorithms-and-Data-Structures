package main

import "strconv"

func compress(chars []byte) int {
	n := len(chars)
	if n == 0 {
		return 0
	}

	writeIndex := 0 // Position to write compressed characters
	readIndex := 0  // Pointer to traverse the array

	for readIndex < n {
		currentChar := chars[readIndex]
		count := 0

		// Count consecutive repeating characters
		for readIndex < n && chars[readIndex] == currentChar {
			readIndex++
			count++
		}

		// Write the character
		chars[writeIndex] = currentChar
		writeIndex++

		// Write the count if > 1
		if count > 1 {
			countStr := strconv.Itoa(count)
			for _, c := range countStr {
				chars[writeIndex] = byte(c)
				writeIndex++
			}
		}
	}

	return writeIndex
}

/*
func main() {
    chars := []byte{'a', 'a', 'b', 'b', 'c', 'c', 'c'}
    length := compress(chars)
    fmt.Println("Compressed Length:", length)        // Output: 6
    fmt.Println("Compressed Array:", string(chars[:length])) // Output: "a2b2c3"
}
*/
