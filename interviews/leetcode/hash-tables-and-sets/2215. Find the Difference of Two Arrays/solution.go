func findDifference(nums1 []int, nums2 []int) [][]int {
	set1 := make(map[int]struct{})
	set2 := make(map[int]struct{})

	// Populate set1 with elements from nums1
	for _, num := range nums1 {
		set1[num] = struct{}{}
	}

	// Populate set2 with elements from nums2
	for _, num := range nums2 {
		set2[num] = struct{}{}
	}

	// Find the elements in set1 but not in set2
	result1 := []int{}
	for num := range set1 {
		if _, exists := set2[num]; !exists {
			result1 = append(result1, num)
		}
	}

	// Find the elements in set2 but not in set1
	result2 := []int{}
	for num := range set2 {
		if _, exists := set1[num]; !exists {
			result2 = append(result2, num)
		}
	}

	return [][]int{result1, result2}
}

/*
func main() {
    nums1 := []int{1, 2, 3}
    nums2 := []int{2, 4, 6}
    fmt.Println(findDifference(nums1, nums2)) // Output: [[1 3] [4 6]]
}
*/
