# n = bits.length
# time = O(n)
# space = O(1)
# done time = 10m


class Solution:

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            flg = 0
            if bits[i] == 1:
                i += 2
            else:
                i += 1
                flg = 1
        return flg == 1
