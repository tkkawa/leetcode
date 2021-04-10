# n = max(s.length, t.length)
# time = O(n)
# space = O(1)
# done time = 30m


class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(moji, n):
            i = 0
            while i < n:
                if moji[i] == "#":
                    if i == 0:
                        moji = moji[1:]
                        i -= 1
                        n -= 1
                    else:
                        moji = moji[:i-1] + moji[i+1:]
                        i -= 2
                        n -= 2
                i += 1
            return moji

        return backspace(s, len(s)) == backspace(t, len(t))
