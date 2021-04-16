# n = s.length
# time = O(n)
# space = O(1)
# done time = 15m


class Solution:

    def checkRecord(self, s: str) -> bool:
        if len(s) - len(s.replace('A', '')) >= 2:
            return False
        L_conti_count = 1
        late = 'L'
        late_limit = 3
        for i in range(1, len(s)):
            if s[i] == late and s[i] == s[i-1]:
                L_conti_count += 1
            else:
                if L_conti_count >= late_limit - 1:
                    L_conti_count = 1
            if L_conti_count >= late_limit:
                return False
        return True
