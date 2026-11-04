class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        ans = []
        maxval = -1

        for i in range(n-1, -1, -1):
            ans.append(maxval)
            maxval = max(maxval, arr[i])

        ans.reverse()
        return ans

                        