class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        mat_size = len(mat)
        middle_index = int((mat_size - 1) / 2)
        ret = 0
        for i in range(mat_size):
            for j in range(mat_size):
                if i == j:
                    ret += mat[i][j]
                    mat[i].reverse()
                    ret += mat[i][j]
        if mat_size % 2 == 1:
            ret -= mat[middle_index][middle_index]
        return ret
