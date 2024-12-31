class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # since the number itself can be zero, multiplying all and then division won't work here
        n = len(nums)
        answer = [1] * n  # Initialize answer array with 1s

        # Step 1: Calculate prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: Calculate postfix products and combine with prefix
        postfix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer
