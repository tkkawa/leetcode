# n = A.length
# time = O(n^2)
# space = O(n)
# done time = 30m
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        for i in range(len(A)):
            A[i] = str(A[i])
        A.reverse()
        res = []
        for i in range(len(A)):
            if int(''.join(A[i:][::-1]), 2)%5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res[::-1]
