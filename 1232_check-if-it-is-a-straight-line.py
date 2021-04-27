# n = coordinates.length
# time = O(n)
# space = O(1)
# done time = 30m


class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(1, len(coordinates)):
            x_diff = coordinates[i][0] - coordinates[0][0]
            if x_diff != 0:
                break

        if x_diff == 0:
            return True
        
        slope = (coordinates[1][1] - coordinates[0][1]) / x_diff
        intercept = coordinates[0][1] - slope*coordinates[0][0]
        
        for coordinate in coordinates:
            y_coordinate = int(slope*coordinate[0] + intercept)
            if y_coordinate != coordinate[1]:
                return False
        
        return True
