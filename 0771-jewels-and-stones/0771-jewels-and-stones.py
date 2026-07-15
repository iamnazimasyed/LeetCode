class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans=0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    ans = ans + 1
                    #Okay, I found one more jewel." Adding 1 increments your running total by exactly one.
                    #f you wrote ans = ans + 2, the program would count each jewel as two, giving you an incorrect total of 6
        return ans
        