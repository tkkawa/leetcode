# n = nums.length
# time = O(n^2)
# space = O(1)
# done time = 1h
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] in nums[i+1:]:
                nums.pop(i)
                n -= 1
                i -= 1
            i += 1
        return len(nums)
'''

# O(n) solution in leetcode
# n = nums.length
# time = O(n)
# space = O(1)


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
