# n = s.length
# time = O(n)
# space = O(1)
class Solution:
    def secondHighest(self, s: str) -> int:
        s = list(s)
        for i in range(len(s)):
            if 96 < ord(s[i]) < 123:
                s[i] = "a"
            else:
                s[i] = int(s[i])
        s = list(set(s))
        if "a" in s:
            s.remove("a")
        if len(s) < 2:
            return -1
        return sorted(s)[-2]
