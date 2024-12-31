class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # compute the largest number of candies
        max_candies = max(candies)

        # create the return array
        # [false] * len(candies)
        return [True if (candy_count+extraCandies>=max_candies) else False for candy_count in candies]
