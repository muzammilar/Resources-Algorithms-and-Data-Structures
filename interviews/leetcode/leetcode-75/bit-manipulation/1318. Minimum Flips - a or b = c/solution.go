package main

// Function to calculate the minimum flips to make a OR b equal to c
func minFlips(a int, b int, c int) int {
	flips := 0
	for i := 0; i < 32; i++ {
		aBit := (a >> i) & 1
		bBit := (b >> i) & 1
		cBit := (c >> i) & 1

		if cBit == 0 {
			// Both aBit and bBit should be 0
			flips += aBit + bBit
		} else {
			// At least one of aBit or bBit should be 1
			if aBit == 0 && bBit == 0 {
				flips += 1
			}
		}
	}
	return flips
}

// Main function (commented out by default)
// func main() {
//     a, b, c := 2, 6, 5
//     fmt.Println(minFlips(a, b, c)) // Output: 3
// }
