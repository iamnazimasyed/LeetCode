class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        minval = nums[0]
        ans = 0
        for i in range(1,len(nums)):
            minval = min(minval, nums[i])
            ans = max(ans,nums[i] - minval)
        if ans <= 0:
            return -1
        else:
            return ans

                