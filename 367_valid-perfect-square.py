# n = num
# time = O(logn)
# space = O(1)
# done time = 20m


class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        low = 1
        high = num

        while low <= high:
            mid = (low + high) >> 1
            square = mid*mid
            if square == num:
                return True
            elif square < num:
                low = mid + 1
            else:
                high = mid - 1

        return False
