# n = n
# time = O(logn)
# space = O(1)
# done time = 20m


class Solution:

    def guessNumber(self, n: int) -> int:
        if guess(n) == 0:
            return n

        low = 1
        high = n
        mid = (low + high) // 2
        while guess(mid) != 0:
            if guess(mid) == -1:
                high = mid
                mid = (low + high) // 2
            if guess(mid) == 1:
                low = mid
                mid = (low + high) // 2
        return mid
