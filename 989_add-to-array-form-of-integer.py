# n = nums.length
# time = O(n)
# space = O(1)
# done time = 15m


class Solution:

    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        nums[-1] += k
        digit_num = len(nums) - 1
        one_digit_max = 9
        while 0 < digit_num and one_digit_max < nums[digit_num]:
            div, mod = divmod(nums[digit_num], one_digit_max + 1)
            nums[digit_num-1] += div
            nums[digit_num] = mod
            digit_num -= 1
        while one_digit_max < nums[0]:
            nums = [nums[0] // (one_digit_max + 1)] + nums
            nums[1] = nums[1] % (one_digit_max + 1)
        return nums
