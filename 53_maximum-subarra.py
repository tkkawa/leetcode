# n = nums.length
# time = 0(n^2)
# space = O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = []
        idx_sub = []
        for i in range(len(nums)):
            sub_nums = nums[i:]
            sub_nums_acc = list(accumulate(sub_nums))
            max_val = max(sub_nums_acc)
            max_idx = sub_nums_acc.index(max_val)
            max_sub.append(max_val)
            idx_sub.append([i, max_idx+i+1])
        res = max_sub.index(max(max_sub))
        return sum(nums[idx_sub[res][0]:idx_sub[res][1]])
