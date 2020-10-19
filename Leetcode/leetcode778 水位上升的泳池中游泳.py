'''
Author: Puffrora
Date: 2020-10-18 23:35:22
LastModifiedBy: Puffrora
LastEditTime: 2020-10-18 23:45:24
'''


# 堆
# 时间复杂度 O(N*N*longN)
# 空间复杂度 O(N*N*longN)
class Solution:
    def swimInWater(self, grid):
        import heapq as hq
        
        def neighbor(r, c):
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= r+dx < len(grid) and 0 <= c+dy < len(grid[0]):
                    yield r+dx, c+dy

        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        res = 0

        while heap:
            val, r, c = hq.heappop(heap)
            res = max(res, val)
            if r == c == len(grid) - 1: return res
            for nr, nc in neighbor(r, c):
                if (nr, nc) not in seen:
                    hq.heappush(heap, (grid[nr][nc], nr, nc))
                    seen.add((nr, nc))
