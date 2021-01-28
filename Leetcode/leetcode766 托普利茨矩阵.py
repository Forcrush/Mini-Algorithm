'''
Author: Puffrora
Date: 2021-01-28 18:26:21
LastModifiedBy: Puffrora
LastEditTime: 2021-01-28 18:29:16
'''


# 时间复杂度 O(M*N)
# 空间复杂度 O(1)
class Solution:
    def isToeplitzMatrix(self, matrix):
        
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if i == 0 or j == 0 or matrix[i][j] == matrix[i-1][j-1]:
                    continue
                else:
                    return False
        return True