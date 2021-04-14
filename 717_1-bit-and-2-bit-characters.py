# n = bits.length
# time = O(n)
# space = O(1)
# done time = 10m


class Solution:

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits):
            is_one_bit_char = False
            if bits[i] == 1:
                i += 2
            else:
                i += 1
                is_one_bit_char = True
        return is_one_bit_char
