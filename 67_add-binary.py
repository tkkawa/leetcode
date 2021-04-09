# n = max(a, b)
# time = O(n)
# space = O(1)
# done time = 10m


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        return bin(int(a, 2) + int(b, 2)).lstrip('0b')
