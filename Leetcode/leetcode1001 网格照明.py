'''
Author: Puffrora
Date: 2021-01-24 13:32:23
LastModifiedBy: Puffrora
LastEditTime: 2021-01-24 14:14:26
'''


class Solution:
    def gridIllumination(self, N, lamps, queries):
        
        from collections import defaultdict

        # 开灯
        lamp_pos = set()
        lighted_pos = defaultdict(int)
        for lx, ly in lamps:
            lamp_pos.add((lx, ly))
            # 记录四个方向上的照亮区域 0 1 2 3 分别代表水平 竖直 45度 -45度方向
            lighted_pos[(0, lx)] += 1
            lighted_pos[(1, ly)] += 1
            lighted_pos[(2, lx+ly)] += 1
            lighted_pos[(3, lx-ly)] += 1
        
        # 查询
        res = []
        for qx, qy in queries:
            if lighted_pos[(0, qx)] or lighted_pos[(1, qy)] or lighted_pos[(2, qx+qy)] or lighted_pos[(3, qx-qy)]:
                res.append(1)
            else:
                res.append(0)
            
            # get neighbor
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = qx+dx, qy+dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if (nx, ny) in lamp_pos:
                            lamp_pos.discard((nx, ny))
                            lighted_pos[(0, nx)] -= lighted_pos[(0, nx)] != 0
                            lighted_pos[(1, ny)] -= lighted_pos[(1, ny)] != 0
                            lighted_pos[(2, nx+ny)] -= lighted_pos[(2, nx+ny)] != 0
                            lighted_pos[(3, nx-ny)] -= lighted_pos[(3, nx-ny)] != 0
                            
        return res
        