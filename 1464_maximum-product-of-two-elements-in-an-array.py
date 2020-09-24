class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] -= 1
        return sorted(nums)[-1] * sorted(nums)[-2]
