class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result = sorted([x*x for x in nums])
        return result
        