'''
Author: Puffrora
Date: 2020-10-16 16:23:57
LastModifiedBy: Puffrora
LastEditTime: 2020-10-16 16:55:27
'''


class Solution:
    def minCostClimbingStairs(self, cost):

        if len(cost) < 3:
            return min(cost)

        f1, f2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            f1, f2 = f2, min(f1, f2) + cost[i]

        return min(f1, f2)
