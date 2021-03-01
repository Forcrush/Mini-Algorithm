'''
Author: Puffrora
Date: 2021-03-01 20:24:03
LastModifiedBy: Puffrora
LastEditTime: 2021-03-01 20:35:07
'''


from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        visited = set()
        row, col = len(matrix), len(matrix[0])

        def get_neighbor(i, j):
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                if 0 <= i+dx < row and 0 <= j+dy < col:
                    yield i+dx, j+dy
        
        queue = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))
        
        cur_depth = 0
        while queue:
            cur_depth += 1
            for _ in range(len(queue)):
                cur_i, cur_j = queue.pop(0)
                for ni, nj in get_neighbor(cur_i, cur_j):
                    if (ni, nj) not in visited:
                        matrix[ni][nj] = cur_depth
                        visited.add((ni, nj))
                        queue.append((ni, nj))
        
        return matrix


