'''
Author: Puffrora
Date: 2021-03-08 22:05:27
LastModifiedBy: Puffrora
LastEditTime: 2021-03-08 22:27:54
'''


from typing import List


# 时间复杂度 O(row * col * min(row, col)) 可根据 row col 大小选择列前缀和还是行前缀和
# 空间复杂度 O(row * col)
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        from collections import defaultdict

        row, col = len(matrix), len(matrix[0])
        res = 0

        # 计算每一列的前缀和
        prefix_col = [[0 for _ in range(col)] for _ in range(row)]
        for c in range(col):
            for r in range(row):
                if r == 0:
                    prefix_col[r][c] = matrix[r][c]
                else:
                    prefix_col[r][c] = prefix_col[r-1][c] + matrix[r][c]
                    
        # 遍历所有起始行 终止行
        for sr in range(row):
            for er in range(sr, row):
                sum_dic = defaultdict(int)
                csum = 0
                for c in range(col):
                    pre = prefix_col[sr-1][c] if sr else 0
                    csum += prefix_col[er][c] - pre
                    if csum == target:
                        res += 1
                    res += sum_dic[csum-target]
                    sum_dic[csum] += 1
        
        return res

