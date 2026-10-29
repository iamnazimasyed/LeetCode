class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        ans = 0
        for i in range(len(colors)-1):
            for j in range(i,len(colors)):
                if colors[i] != colors[j]:
                    temp = j - i
                    ans = max(ans,temp)
        return ans
                