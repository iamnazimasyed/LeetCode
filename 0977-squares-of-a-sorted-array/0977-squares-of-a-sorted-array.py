class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        a = []

        for i in nums:
            a.append(i ** 2)

        a.sort()

        return a
