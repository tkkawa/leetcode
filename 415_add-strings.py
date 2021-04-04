# n = max(num2dd1.length, num2.length)
# time : O(n)
# space : O(1)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        total1 = ord(num1[0])-48
        for i in num1[1:]:
            num = ord(i)-48
            total1 = total1*10+num
        total2 = ord(num2[0])-48
        for i in num2[1:]:
            num = ord(i)-48
            total2 = total2*10+num
        total = total1+total2
        if total == 0:
            return "0"
        text = ""
        while total != 0:
            total, remain = divmod(total,10)
            text += (chr(remain+48))
        return text[::-1]
