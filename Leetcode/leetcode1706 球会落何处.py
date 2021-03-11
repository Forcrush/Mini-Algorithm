'''
Author: Puffrora
Date: 2021-03-10 14:17:15
LastModifiedBy: Puffrora
LastEditTime: 2021-03-11 09:58:07
'''


from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        R, C = len(grid), len(grid[0])
        # 模拟小球掉落
        def simulation(row, col, flag):

            if grid[row][col] == 1:
                if flag == 'V':
                    if col == C - 1 or grid[row][col+1] == -1:
                        return -1
                    else:
                        return simulation(row, col+1, 'H')
                if flag == 'H':
                    if row == R - 1:
                        return col
                    else:
                        return simulation(row+1, col, 'V')
            
            if grid[row][col] == -1:
                if flag == 'V':
                    if col == 0 or grid[row][col-1] == 1:
                        return -1
                    else:
                        return simulation(row, col-1, 'H')
                if flag == 'H':
                    if row == R - 1:
                        return col
                    else:
                        return simulation(row+1, col, 'V')
            
        res = []
        for i in range(C):
            res.append(simulation(0, i, 'V'))
        
        return res
