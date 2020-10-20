# n = nums_set.length
# m = nums.count(i)
# time : O(n*m)
# space : O(n)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def kaijo(n, k=2):
            if n == 1:
                return n
            return n * kaijo(n-1)
        nums_set = list(set(nums))
        ret = 0
        for i in nums_set:
            if nums.count(i) == 1:
                continue
            if nums.count(i) == 2:
                ret += 1
                continue
            ret += kaijo(nums.count(i))/(kaijo(nums.count(i) - 2) * 2)
            
        return int(ret)
