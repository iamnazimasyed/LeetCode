class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        ans = 0
        for i in nums:
            ans = ans + i 
            result.append(ans)
        return result
        