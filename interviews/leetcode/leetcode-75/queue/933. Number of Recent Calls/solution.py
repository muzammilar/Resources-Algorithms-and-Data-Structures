
PAST_TIME_SECONDS = 3000

class RecentCounter:
    def __init__(self):
        self.calls = []  # List to store the timestamps of the calls

    def ping(self, t: int) -> int:
        # Add the current call timestamp
        self.calls.append(t)

        # Remove calls that are outside the  window
        while self.calls[0] < t - PAST_TIME_SECONDS:
            self.calls.pop(0)

        # The size of the list represents the number of recent calls
        return len(self.calls)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Test the solution
# if __name__ == "__main__":
#     recentCounter = RecentCounter{}
#     print(recentCounter.ping(1))      # Output: 1
#     print(recentCounter.ping(100))    # Output: 2
#     print(recentCounter.ping(3001))   # Output: 3
#     print(recentCounter.ping(3002))   # Output: 3
