class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        result = []
        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(nums[i])
        zeros = len(nums) - len(result)
        result.extend([0] * zeros)
        nums[:] = result
                