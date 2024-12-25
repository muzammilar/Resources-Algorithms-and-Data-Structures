from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()  # Queue for Radiant senators
        dire = deque()     # Queue for Dire senators

        # Initialize the queues with the indices of the senators
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Process the senators until one faction wins
        while radiant and dire:
            # Get the indices of the senators at the front of both queues
            r = radiant.popleft()
            d = dire.popleft()

            # The senator with the smaller index gets to ban the other
            if r < d:
                radiant.append(r + len(senate))  # Reinsert the Radiant senator at the end of the queue
            else:
                dire.append(d + len(senate))    # Reinsert the Dire senator at the end of the queue

        # If Radiant still has senators, they win; otherwise, Dire wins
        return "Radiant" if radiant else "Dire"

# Test the solution
# if __name__ == "__main__":
#     solution = Solution()
#     print(solution.predictPartyVictory("RD"))  # Output: "Radiant"
#     print(solution.predictPartyVictory("RDD"))  # Output: "Dire"
