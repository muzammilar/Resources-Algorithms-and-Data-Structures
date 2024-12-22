def maxOperations(nums, k):
    nums.sort()  # Sort the array
    left, right = 0, len(nums) - 1
    pairs = 0

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == k:
            pairs += 1
            left += 1
            right -= 1
        elif current_sum < k:
            left += 1
        else:
            right -= 1

    return pairs

# Example usage
nums = [1, 2, 3, 4, 5]
k = 5
print(maxOperations(nums, k))  # Output: 2
