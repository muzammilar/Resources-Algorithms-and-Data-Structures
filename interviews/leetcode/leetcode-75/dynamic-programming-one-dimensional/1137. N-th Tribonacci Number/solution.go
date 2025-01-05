package main

// tribonacci function calculates the n-th Tribonacci number
func tribonacci(n int) int {
	// Base cases for n = 0, 1, and 2
	if n == 0 {
		return 0
	} else if n == 1 || n == 2 {
		return 1
	}

	// Initialize the first three Tribonacci numbers
	t0, t1, t2 := 0, 1, 1
	t_next := 0 // To store the next Tribonacci number

	// Calculate the Tribonacci number for n >= 3
	for i := 3; i <= n; i++ {
		// The next Tribonacci number is the sum of the previous three
		t_next = t0 + t1 + t2
		// Update the previous three numbers
		t0, t1, t2 = t1, t2, t_next
	}

	return t_next
}

func main() {
	// Uncomment the following lines to test the code:
	// fmt.Println(tribonacci(4))  // Example input
}
