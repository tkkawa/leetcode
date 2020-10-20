# n = cpdomain.length
# m = moji.length
# time : O(n*m)
# space : O(dic.key nums))
from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = Counter()
        ret = []
        for i in cpdomains:
            spl = i.split(' ')
            moji = spl[1].split('.')
            mojiretu = moji[-1]
            dic[mojiretu] += int(spl[0])
            spl.pop()
            for j in reversed(range(len(moji)-1)):
                mojiretu = moji[j] + "." + mojiretu
                dic[mojiretu] += int(spl[0])
        for moji, num in dic.items():
            ret.append(str(num) + " " + moji)
        return ret
