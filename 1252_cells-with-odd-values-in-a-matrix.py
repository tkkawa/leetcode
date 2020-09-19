import numpy as np
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = np.zeros((n, m))
        for i in range(len(indices)):
            mat[indices[i][0], :] += 1
            mat[:, indices[i][1]] += 1
        ret = 0
        for i in range(n):
            for j in range(m):
                if mat[i, j] % 2 == 1:
                    ret += 1
        return ret
