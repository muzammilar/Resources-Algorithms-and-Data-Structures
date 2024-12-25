package main

const maxTimeSeconds = 3000

type RecentCounter struct {
	calls []int
}

func Constructor() RecentCounter {
	return RecentCounter{}
}

func (this *RecentCounter) Ping(t int) int {
	// Add the current call timestamp
	this.calls = append(this.calls, t)

	// Remove calls that are outside the maxTimeSeconds window
	for len(this.calls) > 0 && this.calls[0] < t-maxTimeSeconds {
		this.calls = this.calls[1:]
	}

	// The length of the calls slice is the number of recent calls
	return len(this.calls)
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */

// Uncomment to run the solution and test cases
// func main() {
//     recentCounter := Constructor()
//     fmt.Println(recentCounter.Ping(1))      // Output: 1
//     fmt.Println(recentCounter.Ping(100))    // Output: 2
//     fmt.Println(recentCounter.Ping(3001))   // Output: 3
//     fmt.Println(recentCounter.Ping(3002))   // Output: 3
// }
