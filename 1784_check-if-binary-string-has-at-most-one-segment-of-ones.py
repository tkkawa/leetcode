# n = s.length
# time = O(n)
# space = O(1)
# done time = 20m


class Solution:

    def checkOnesSegment(self, s: str) -> bool:
        continuous_count = 1
        one_count = s.count('1')
        for i in range(1, len(s)):
            if s[i] == '1' and s[i] == s[i-1]:
                continuous_count += 1
        return continuous_count == one_count
