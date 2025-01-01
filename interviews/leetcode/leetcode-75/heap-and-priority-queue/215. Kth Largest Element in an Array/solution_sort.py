import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Step 1: Use a min-heap of size k
        min_heap = []

        # Step 2: Iterate through each number in the array
        for num in nums:
            # Step 3: Add the number to the heap
            heapq.heappush(min_heap, num)

            # Step 4: If the size of the heap exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Step 5: The root of the heap will contain the kth largest element
        return min_heap[0]

# Uncomment the following lines to test the function
# print(Solution().findKthLargest([3,2,1,5,6,4], 2))  # Expected output: 5
# print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # Expected output: 4
