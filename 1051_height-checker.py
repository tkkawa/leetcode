class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sort = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != heights_sort[i]:
                count += 1
        return count
