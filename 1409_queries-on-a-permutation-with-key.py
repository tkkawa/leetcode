# n = queries.length
# time : O(n^2)
# space : O(n+m)
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1, m+1)]
        ret = []
        for que in queries:
            ind = P.index(que)
            ret.append(ind)
            P.pop(ind)
            P.insert(0, que)
        return ret
