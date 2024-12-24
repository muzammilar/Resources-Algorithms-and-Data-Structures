class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)  # Convert nums1 to a set
        set2 = set(nums2)  # Convert nums2 to a set
        # diff = list(set(nums1) ^ set(nums2)) # XOR Trick - This will generate a single list insteat of two nested lists
        diff = [list(set1 - set2), list(set2 - set1)]
        return diff
