'''
Author: Puffrora
Date: 2020-10-17 20:44:35
LastModifiedBy: Puffrora
LastEditTime: 2020-10-17 21:41:09
'''


class Solution:
    def cherryPickup(self, grid):

        R, C = len(grid), len(grid[0])

        dp = [[[0 for _ in range(C)] for _ in range(C)] for _ in range(R)]
        
        def neighbor(bot1, bot2):
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if 0 <= bot1+i < C and 0 <= bot2+j < C:
                        yield bot1+i, bot2+j

        def search(r, bot1, bot2):
            if r == R-1:
                memo[(r, bot1, bot2)] = grid[r][bot1] + \
                    (bot1 != bot2) * grid[r][bot2]
                return memo[(r, bot1, bot2)]

            res = grid[r][bot1] + (bot1 != bot2) * grid[r][bot2]
            tmp = 0
            for p1, p2 in neighbor(bot1, bot2):
                if (r+1, p1, p2) in memo:
                    tmp = max(tmp, memo[(r+1, p1, p2)])
                else:
                    tmp = max(tmp, search(r+1, p1, p2))
            res += tmp

            memo[(r, bot1, bot2)] = res
            return res
        
        memo = {(0, 0, C-1): grid[0][0] + grid[0][C-1]}

        return search(0, 0, C-1)
