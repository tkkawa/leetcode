# n = coordinates.length
# time = O(n)
# space = O(1)
# done time = 30m


class Solution:

    def checkStraightLine(self, arr: List[List[int]]) -> bool:
        N = len(arr)
        return all(
            (arr[i + 1][1] - arr[i][1]) * (arr[i + 2][0] - arr[i + 1][0]) ==
            (arr[i + 1][0] - arr[i][0]) * (arr[i + 2][1] - arr[i + 1][1])
            for i in range(N - 2)
        )
