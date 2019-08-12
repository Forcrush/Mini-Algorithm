# =========================================================================
# Andrew's Monotone Chain Convex Hull Algorithm(复杂度降低)
# Link: http://www.algorithmist.com/index.php/Monotone_Chain_Convex_Hull

# LeetCode 587
class Solution:
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        N = len(points)
        if N <= 3: 
            return points
        lb = min(points, key = lambda p: (p.y, p.x))
        ccw = lambda p1, p2, p3: (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)
        points.sort(key = lambda p: (p.x, p.y))
        lo = []
        for x in range(N):
            while len(lo) > 1 and ccw(lo[-2], lo[-1], points[x]) < 0:
                lo.pop()
            lo.append(points[x])
        up = []
        for x in range(N - 1, -1, -1):
            while len(up) > 1 and ccw(up[-2], up[-1], points[x]) < 0:
                up.pop()
            up.append(points[x])
        return lo[:-1] + up[:-1]
