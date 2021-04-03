# n = min(num1.length, num2.length)
# m = max(num1,length, num2.length)
# time : O(n)
# space : O(m)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        lis1 = list(num1)[::-1]
        lis2 = list(num2)[::-1]
        res = []
        a = 0
        for i in range(min(len(lis1), len(lis2))):
            res.append(num.index(lis1[i]) + num.index(lis2[i]))
            if i == len(lis1)-1:
                lis = lis2
            if i == len(lis2)-1:
                lis = lis1
        if len(lis) != len(res):
            for i in range(len(res), len(res)+max(len(lis1), len(lis2))-min(len(lis1), len(lis2))):
                res.append(num.index(lis[i]))
        a = 1
        sum = 0
        for i in range(len(res)):
            sum += a * res[i]
            a *= 10
        return str(sum)
