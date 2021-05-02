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
        mid = (low + high) >> 1
        while low < high:
            guess_low_high = guess(mid)
            if guess_low_high == -1:
                high = mid
                mid = (low + high) >> 1
            elif guess_low_high == 1:
                low = mid
                mid = (low + high) >> 1
            else:
                low += 1
        return mid