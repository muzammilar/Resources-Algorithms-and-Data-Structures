package main

// Function to find the length of the longest common subsequence
func longestCommonSubsequence(text1 string, text2 string) int {
	m, n := len(text1), len(text2)

	// Use two 1D arrays for space optimization
	dpPrev := make([]int, n+1)
	dpCurr := make([]int, n+1)

	// Fill the dp table
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if text1[i-1] == text2[j-1] {
				dpCurr[j] = dpPrev[j-1] + 1
			} else {
				dpCurr[j] = max(dpPrev[j], dpCurr[j-1])
			}
		}
		// Swap the current and previous row
		dpPrev, dpCurr = dpCurr, dpPrev
	}

	return dpPrev[n]
}

// Main function (commented out by default)
// func main() {
//     text1 := "abcde"
//     text2 := "ace"
//     fmt.Println(longestCommonSubsequence(text1, text2)) // Output: 3
// }
