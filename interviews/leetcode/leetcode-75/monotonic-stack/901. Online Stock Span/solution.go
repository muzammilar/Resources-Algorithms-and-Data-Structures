package main

// StockSpanner represents the stock span system.
type StockSpanner struct {
	stack []struct {
		price int
		span  int
	}
}

// Constructor creates a new instance of StockSpanner.
func Constructor() StockSpanner {
	return StockSpanner{}
}

// Next calculates the stock span for the current price.
func (this *StockSpanner) Next(price int) int {
	span := 1
	// While the stack is not empty and the current price is greater than or equal to the price at the top of the stack
	for len(this.stack) > 0 && price >= this.stack[len(this.stack)-1].price {
		// Pop the stack and add its span to the current span
		span += this.stack[len(this.stack)-1].span
		this.stack = this.stack[:len(this.stack)-1]
	}
	// Push the current price and its span to the stack
	this.stack = append(this.stack, struct {
		price int
		span  int
	}{price, span})
	return span
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */

// Main function (commented out by default)
// func main() {
//     spanner := Constructor()
//     fmt.Println(spanner.Next(100)) // Output: 1
//     fmt.Println(spanner.Next(80))  // Output: 1
//     fmt.Println(spanner.Next(60))  // Output: 1
//     fmt.Println(spanner.Next(70))  // Output: 2
//     fmt.Println(spanner.Next(60))  // Output: 1
//     fmt.Println(spanner.Next(75))  // Output: 4
//     fmt.Println(spanner.Next(85))  // Output: 6
// }
