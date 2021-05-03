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
            return_val_by_guess = guess(mid)
            if return_val_by_guess == -1:
                high = mid
                mid = (low + high) >> 1
            elif return_val_by_guess == 1:
                low = mid
                mid = (low + high) >> 1
            else:
                low += 1
        return mid
