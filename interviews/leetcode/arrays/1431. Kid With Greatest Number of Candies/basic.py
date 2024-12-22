class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # compute the largest number of candies
        max_candies = max(candies)

        # create the return array
        # [false] * len(candies)
        return [True if (candy_count+extraCandies>=max_candies) else False for candy_count in candies]
