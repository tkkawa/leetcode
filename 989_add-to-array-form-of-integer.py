# n = nums.length
# time = O(n)
# space = O(n)
# done time = 15m


class Solution:

    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        num = ""
        for n in nums:
            num += str(n)
        ret_num = str(int(num) + k)
        ret = []
        for n in ret_num:
            ret.append(int(n))
        return ret
