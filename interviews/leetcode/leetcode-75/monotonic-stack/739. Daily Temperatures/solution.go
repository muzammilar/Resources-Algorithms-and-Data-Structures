package main

func dailyTemperatures(temperatures []int) []int {
	// Initialize the result array
	result := make([]int, len(temperatures))
	// Initialize an empty stack to hold indices
	stack := []int{}

	// Iterate through the temperatures
	for i := 0; i < len(temperatures); i++ {
		// While the stack is not empty and the current temperature is greater
		// than the temperature at the index at the top of the stack
		for len(stack) > 0 && temperatures[i] > temperatures[stack[len(stack)-1]] {
			// Pop the top index and calculate the number of days to wait
			idx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			result[idx] = i - idx
		}
		// Push the current index onto the stack
		stack = append(stack, i)
	}

	return result
}

// Main function (commented out by default)
// func main() {
//     temperatures := []int{73, 74, 75, 71, 69, 72, 76, 73}
//     result := dailyTemperatures(temperatures)
//     fmt.Println(result)  // Output: [1 1 4 2 1 1 0 0]
// }
