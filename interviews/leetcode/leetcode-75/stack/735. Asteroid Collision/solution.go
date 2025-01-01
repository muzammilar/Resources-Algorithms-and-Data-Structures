package main

func asteroidCollision(asteroids []int) []int {
	stack := []int{} // Stack to track asteroids in the current state

	for _, asteroid := range asteroids {

		asteroidDestroyed := false
		// Process the current asteroid
		for len(stack) > 0 && asteroid < 0 && stack[len(stack)-1] > 0 {
			// Handle the collision between the asteroid and the one in the stack
			top := stack[len(stack)-1]
			if top < -asteroid {
				// The current asteroid destroys the one in the stack
				stack = stack[:len(stack)-1]
				continue
			}
			// Both asteroids are destroyed
			if top == -asteroid {
				stack = stack[:len(stack)-1]
			}
			// if asteroid is smaller or equal, break the loop
			asteroidDestroyed = true
			break
		}
		// No collision, or asteroid is moving right (positive), so just add it to the stack
		if asteroid > 0 || !asteroidDestroyed {
			stack = append(stack, asteroid)
		}
	}

	return stack
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// Uncomment to run the solution and test cases
// func main() {
//     // Example test case
//     asteroids := []int{5, 10, -5}
//     result := asteroidCollision(asteroids)
//     fmt.Println(result) // Output: [5, 10]
// }
