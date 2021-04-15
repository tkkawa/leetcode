# n = nums.length
# time = O(n)
# space = O(n)
# done time = 15m


class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        if sum(nums[1:]) == 0:
            return 0
        acc_nums = list(accumulate(nums))
        for i in range(0, len(nums)-1):
            if nums_sum == acc_nums[i]*2 + nums[i+1]:
                return i + 1
        return -1
