class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] -= 1
        nums.sort()
        return nums[-1] * nums[-2]
