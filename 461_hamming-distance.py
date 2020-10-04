class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x2 = list(bin(x))
        y2 = list(bin(y))
        x2.remove('b')
        y2.remove('b')
        x2.reverse()
        y2.reverse()
        if len(x2) != len(y2):
            for i in range(max(len(x2),len(y2))):
                if len(x2) < len(y2):
                    x2.append('0')
                elif len(x2) > len(y2):
                    y2.append('0')
        count = 0
        for i in range(len(x2)):
            if x2[i] != y2[i]:
                count += 1
        return count
