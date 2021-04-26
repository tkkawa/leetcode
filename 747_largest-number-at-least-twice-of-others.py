# n = nums.length
# time = O(n)
# space = O(1)
# done time = 5m


class Solution:

    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        max_idx = nums.index(max_num)
        for i, num in enumerate(nums):
            if i == max_idx:
                continue
            if max_num // 2 < num:
                return -1
        return max_idx
