# n = num.length
# time = O(n)
# space = O(1)
# done time = 20m


class Solution:

    def convertToBase7(self, num: int) -> str:
        shou = 1
        ret = ''
        num_kari = num
        while shou > 0:
            if num < 0:
                shou, amari = divmod(-num, 7)
            else:
                shou, amari = divmod(num, 7)
            ret = str(amari) + ret
            num = shou
        if num_kari < 0:
            ret = '-' + ret
        return ret
