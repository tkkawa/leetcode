# n = n
# time = O(n)
# space = O(1)
# done time = 10m


class Solution:

    def arrangeCoins(self, n: int) -> int:
        step = 1
        while 0 < n:
            n -= step
            step += 1
        step -= 1

        if n == 0:
            return step

        return step - 1
