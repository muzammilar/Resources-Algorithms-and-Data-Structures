func kidsWithCandies(candies []int, extraCandies int) []bool {
	// find the total number of candies
	maxCandies := maxVal(candies)

	// create the return array
	retArr := make([]bool, len(candies))

	// compute the new max value for each
	for i := 0; i < len(candies); i++ {
		retArr[i] = false
		if maxCandies <= candies[i]+extraCandies {
			retArr[i] = true
		}
	}
	return retArr
}

func maxVal(arr []int) int {
	mx := 0
	for i := 0; i < (len(arr)); i++ {
		mx = max(mx, arr[i])
	}
	return mx
}
