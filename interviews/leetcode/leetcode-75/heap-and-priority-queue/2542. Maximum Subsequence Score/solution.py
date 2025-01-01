import heapq

class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # Step 1: Create pairs of corresponding elements from nums1 and nums2
        n = len(nums1)
        pairs = list(zip(nums1, nums2))

        # Step 2: Sort pairs in descending order by the values from nums2
        pairs.sort(reverse=True, key=lambda x: x[1])

        # Step 3: Initialize variables for the heap and the current sum of the nums1 values
        heap = []  # Min-heap to store nums1 values
        current_sum = 0  # Sum of selected nums1 values
        max_score = 0  # To store the maximum score encountered

        # Step 4: Iterate over the sorted pairs
        for num1, num2 in pairs:
            # Add current num1 to the heap and increase the current sum
            heapq.heappush(heap, num1)
            current_sum += num1

            # If the heap size exceeds k, remove the smallest nums1 value (to keep at most k elements)
            if len(heap) > k:
                current_sum -= heapq.heappop(heap)

            # Calculate the score of the current subsequence (sum of nums1 values * num2)
            if len(heap) == k:  # Only calculate the score when we have exactly k elements
                max_score = max(max_score, current_sum * num2)  # Multiply by the current num2 value

        return max_score

# Main function (commented out by default)
# if __name__ == "__main__":
#     solution = Solution()
#     nums1 = [1, 3, 4, 5]
#     nums2 = [2, 4, 1, 6]
#     k = 3
#     print(solution.maxScore(nums1, nums2, k))  # Expected output: 14
