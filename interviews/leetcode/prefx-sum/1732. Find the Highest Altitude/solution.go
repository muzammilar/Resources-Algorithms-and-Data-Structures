func largestAltitude(gain []int) int {
	maxAltitude := 0
	currentAltitude := 0

	for _, g := range gain {
		currentAltitude += g
		maxAltitude = max(maxAltitude, currentAltitude)
	}

	return maxAltitude
}

/*
func main() {
    gain := []int{-5, 1, 5, 0, -7}
    fmt.Println(largestAltitude(gain)) // Output: 1
}
*/
