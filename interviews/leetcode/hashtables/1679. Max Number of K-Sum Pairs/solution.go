func maxOperations(nums []int, k int) int {
	freq := make(map[int]int)
	pairs := 0

	for _, num := range nums {
		complement := k - num
		if freq[complement] > 0 {
			pairs++
			freq[complement]--
		} else {
			freq[num]++
		}
	}

	return pairs
}
