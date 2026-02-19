class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if not points:
            return 0

        points.sort(key=lambda x: (x[0], x[1]))

        count = 0
        temp = []
        i = 0

        while i < len(points):
            l, r = points[i]

            if not temp:
                temp = [l, r]
                i += 1
                continue

            if l <= temp[1]:
                temp[1] = min(temp[1], r)
                i += 1
            else:
                count += 1
                temp = []

        return count + 1
