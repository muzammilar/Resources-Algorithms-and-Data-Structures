import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        # Priority queue to store costs with their respective indices
        priority_queue = []
        n = len(costs)  # The total number of costs provided

        # Calculate the boundary indices for the candidates
        left_candidate_bound = candidates - 1
        right_candidate_bound = n - candidates

        # Populate the priority queue with the left side candidates
        for index in range(candidates):
            priority_queue.append((costs[index], index))

        # Populate the priority queue with the right side candidates
        for index in range(n - candidates, n):
            # Only add if we're past 'left_candidate_bound'
            if index > left_candidate_bound:
                priority_queue.append((costs[index], index))

        # Transform the priority_queue into a min-heap
        heapq.heapify(priority_queue)

        # Variable to keep the running total cost of the selected candidates
        total_cost = 0

        # Retrieve the smallest costs 'k' times
        for _ in range(k):
            # Extract the candidate with the smallest cost
            cost, index = heapq.heappop(priority_queue)
            total_cost += cost

            # If selected from the left side, we need to move the left boundary right
            if index <= left_candidate_bound:
                left_candidate_bound += 1
                if left_candidate_bound < right_candidate_bound:
                    heapq.heappush(priority_queue, (costs[left_candidate_bound], left_candidate_bound))

            # If selected from the right side, we need to move the right boundary left
            if index >= right_candidate_bound:
                right_candidate_bound -= 1
                if left_candidate_bound < right_candidate_bound:
                    heapq.heappush(priority_queue, (costs[right_candidate_bound], right_candidate_bound))

        return total_cost

# Main function (commented out by default)
# if __name__ == "__main__":
#     solution = Solution()
#     costs = [1, 3, 5, 2, 8, 6]
#     k = 3
#     candidates = 2
#     print(solution.totalCost(costs, k, candidates))  # Expected output: 10
