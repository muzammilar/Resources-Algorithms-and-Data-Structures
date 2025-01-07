class StockSpanner:

    def __init__(self):
        # Initialize an empty stack to store (price, span) pairs
        self.stack = []

    def next(self, price: int) -> int:
        # Initialize the span for the current price to 1
        span = 1
        # While the stack is not empty and the current price is greater than or equal to the price at the top of the stack
        while self.stack and self.stack[-1][0] <= price:
            # Pop the stack and add its span to the current span
            span += self.stack.pop()[1]
        # Push the current price and its span to the stack
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# Main function (commented out by default)
# def main():
#     spanner = StockSpanner()
#     print(spanner.next(100))  # Output: 1
#     print(spanner.next(80))   # Output: 1
#     print(spanner.next(60))   # Output: 1
#     print(spanner.next(70))   # Output: 2
#     print(spanner.next(60))   # Output: 1
#     print(spanner.next(75))   # Output: 4
#     print(spanner.next(85))   # Output: 6
