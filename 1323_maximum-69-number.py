class Solution:
    def maximum69Number (self, num: int) -> int:
        num_st = list(str(num))
        if '6' not in num_st:
            return num
        else:
            num_len = len(num_st)
            ret = []
            num_st_copy = num_st.copy()
            for i in range(num_len):
                if num_st[i] == '9':
                    num_st[i] = '6'
                else:
                    num_st[i] = '9'
                ret.append(int("".join(num_st)))
                num_st = num_st_copy.copy()
            return max(ret)
