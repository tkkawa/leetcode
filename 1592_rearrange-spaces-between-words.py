# n = test.length
# time = O(n)
# space = O(n)
# done time = 20m


class Solution:

    def reorderSpaces(self, text: str) -> str:
        space_num = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return words[0] + " "*space_num
        space_num_divide, space_mod = divmod(space_num, len(words) - 1)
        ret = ""
        for word in words:
            ret = ret + word + " "*space_num_divide
        ret = ret.rstrip()
        ret = ret + " "*space_mod
        return ret
