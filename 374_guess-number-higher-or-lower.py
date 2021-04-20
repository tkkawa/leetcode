# n = n
# time = O(logn)
# space = O(1)
# done time = 20m


class Solution:

    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while guess(n) != 0:
            if guess(n) == -1:
                high = n
                n = (low + high) // 2
            elif guess(n) == 1:
                low = n
                n = (low + high) // 2
        return n
