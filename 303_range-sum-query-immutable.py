# n = nums.length
# time = O(n)
# space = O(1)
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.res = None
        
    def sumRange(self, left: int, right: int) -> int:
        self.res = sum(self.nums[left:right+1])
        return self.res
