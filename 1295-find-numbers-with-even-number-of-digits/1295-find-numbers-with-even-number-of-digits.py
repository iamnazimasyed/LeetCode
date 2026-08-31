class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            ans = len(str(num))

            if ans % 2 == 0:
                count = count + 1
        
        return count

    

        