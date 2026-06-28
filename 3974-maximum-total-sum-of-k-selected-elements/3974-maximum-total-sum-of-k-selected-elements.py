class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)

        current=0
        for i in range(k):
            if mul>1:
                current+=nums[i]*mul
                mul-=1
            else:
                current+=nums[i]
        return current