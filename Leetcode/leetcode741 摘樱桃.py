'''
Author: Puffrora
Date: 2020-10-13 13:11:54
LastModifiedBy: Puffrora
LastEditTime: 2020-10-13 16:01:05
'''

"""
与其从左上角走到右下角，再从右下角走到左上角；不如直接考虑从左上角选两条路走到右下角。
在走了 t 步之后，我们可能处于的位置(r, c) 满足 r+c = t，所以如果我们在位置(r1, c1) 和(r2, c2) 有两个人，
那么 r2 = r1+c1-c2。这意味着 r1，c1，c2 唯一地决定了两个走了 t 步数的人。这个条件让我们能够很好地进行动态规划。

算法：
定义 dp[r1][c1][c2] 是两个人从(r1, c1) 和(r2, c2) 开始，朝着(N-1, N-1) 所能摘到最多的樱桃数量，其中 r2 = r1+c1-c2。
如果 grid[r1][c1] 和 grid[r2][c2] 不是荆棘，那么 dp[r1][c1][c2] 的值是(grid[r1][c1] + grid[r2][c2])，
加上 dp[r1+1][c1][c2]，dp[r1][c1+1][c2]，dp[r1+1][c1][c2+1]，dp[r1][c1+1][c2+1] 的最大值。在(r1, c1) == (r2, c2) 的情况下，我们要避免重复计数。
为什么要加上 dp[r+1][c1][c2]，dp[r1][c1+1][c2]，dp[r1+1][c1][c2+1]，dp[r1][c1+1][c2+1]的最大值？它对应 1 号和人 2 号向下或向右移动的 4 种可能性：
> 1 号向下和 2 号向下：dp[r1+1][c1][c2]
> 1 号向右和 2 号向下：dp[r1][c1+1][c2]
> 1 号向下和 2 号向右：dp[r1+1][c1][c2+1]
> 1 号向右和 2 号向右：dp[r1][c1+1][c2+1]
"""
class Solution:
    def cherryPickup(self, grid):
        # 因为是 N*N 网格
        N = len(grid)
        dp = [[[None for _ in range(N)] for _ in range(N)] for _ in range(N)]

        def find(r1, c1, c2):
            r2 = r1 + c1 - c2

            # 如果到边界或遇到荆棘
            if N in (r1, c1, r2, c2) or -1 in (grid[r1][c1], grid[r2][c2]):
                return float('-inf')
            # 到终点
            elif r1 == c1 == N-1:
                return grid[r1][c1]
            elif dp[r1][c1][c2] != None:
                return dp[r1][c1][c2]
            else:
                res = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                res += max(find(r1, c1+1, c2+1), find(r1+1, c1, c2+1),
                           find(r1, c1+1, c2), find(r1+1, c1, c2))
            dp[r1][c1][c2] = res

            return res
        
        return max(0, find(0, 0, 0))


# @ testing 贪心算法的反例
grid = [
[1,1,1,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,1],
[1,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0],
[0,0,0,1,1,1,1]]

print(Solution().cherryPickup(grid))


