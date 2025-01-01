package main

import (
	"math"
)

type SmallestInfiniteSet struct {
	addedBack    map[int]bool
	nextSmallest int
}

func Constructor() SmallestInfiniteSet {
	return SmallestInfiniteSet{
		addedBack:    make(map[int]bool),
		nextSmallest: 1,
	}
}

func (this *SmallestInfiniteSet) AddBack(n int) {
	// Add n back if it's smaller than the next smallest number
	if n < this.nextSmallest {
		this.addedBack[n] = true
	}
}

func (this *SmallestInfiniteSet) PopSmallest() int {
	var smallest int
	// If there are numbers that were added back, return the smallest one
	if len(this.addedBack) > 0 {
		smallest = math.MaxInt
		for num := range this.addedBack {
			if num < smallest {
				smallest = num
			}
		}
		delete(this.addedBack, smallest)
	} else {
		// Otherwise, return the next smallest number and increment it
		smallest = this.nextSmallest
		this.nextSmallest++
	}
	return smallest
}

// Uncomment the following lines to test the function
// obj := Constructor()
// obj.AddBack(2)
// fmt.Println(obj.PopSmallest())  // Expected output: 1
// fmt.Println(obj.PopSmallest())  // Expected output: 2
// obj.AddBack(1)
// fmt.Println(obj.PopSmallest())  // Expected output: 3
// fmt.Println(obj.PopSmallest())  // Expected output: 4
