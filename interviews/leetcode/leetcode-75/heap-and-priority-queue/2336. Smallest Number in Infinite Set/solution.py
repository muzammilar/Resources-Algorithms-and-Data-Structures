class SmallestInfiniteSet:

    def __init__(self):
        self.added_back = set()  # Set to store the numbers that have been added back
        self.next_smallest = 1  # The next smallest number to be popped

    def addBack(self, n: int) -> None:
        # If the number is greater than or equal to next_smallest, no need to add it back
        if n < self.next_smallest:
            self.added_back.add(n)

    def popSmallest(self) -> int:
        if self.added_back:
            smallest = min(self.added_back)  # Get the smallest element in the added_back set
            self.added_back.remove(smallest)
        else:
            smallest = self.next_smallest  # Otherwise, take the next smallest number
            self.next_smallest += 1  # Increment the next smallest number
        return smallest

# Uncomment the following lines to test the function
# obj = SmallestInfiniteSet()
# obj.addBack(2)
# print(obj.popSmallest())  # Expected output: 1
# print(obj.popSmallest())  # Expected output: 2
# obj.addBack(1)
# print(obj.popSmallest())  # Expected output: 3
# print(obj.popSmallest())  # Expected output: 4
