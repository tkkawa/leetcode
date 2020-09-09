class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = []
        sum = 0
        for i in nums:
            sum += i
            ret.append(sum)
        return ret
