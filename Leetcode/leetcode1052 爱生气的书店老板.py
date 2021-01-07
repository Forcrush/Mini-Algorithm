'''
Author: Puffrora
Date: 2021-01-07 20:26:29
LastModifiedBy: Puffrora
LastEditTime: 2021-01-07 21:22:13
'''


class Solution:
    def maxSatisfied(self, customers, grumpy, X):

        res = 0
        time_point = []
        prefix_sum = []
        for i in range(len(grumpy)):
            if grumpy[i]:
                time_point.append(i)
                prefix_sum.append(customers[i])
            else:
                res += customers[i]
        
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
        
        start = grumpy_cus = 0
        for end in range(len(time_point)):
            while time_point[end] - time_point[start] >= X:
                start += 1
            grumpy_cus = max(grumpy_cus, prefix_sum[end]-prefix_sum[start]+customers[time_point[start]])
        
        res += grumpy_cus

        return res

