'''
Author: Puffrora
Date: 2021-02-26 09:42:27
LastModifiedBy: Puffrora
LastEditTime: 2021-02-26 10:20:02
'''


# 时间复杂度 O(row^2)
# 空间复杂度 O(row^2)
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # 因为最多 100 层
        amount = [[0 for _ in range(101)] for _ in range(101)]
        amount[0][0] = poured
        for r in range(query_row+1):
            for c in range(r+1):
                if amount[r][c] > 1:
                    overflow = (amount[r][c] - 1) / 2
                    amount[r+1][c] += overflow
                    amount[r+1][c+1] += overflow
        
        return min(1, amount[query_row][query_glass])

