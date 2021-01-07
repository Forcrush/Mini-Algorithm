'''
Author: Puffrora
Date: 2021-01-07 21:41:40
LastModifiedBy: Puffrora
LastEditTime: 2021-01-07 21:59:21
'''


class Solution:
    def distributeCandies(self, candies, num_people):
        
        res = [0] * num_people

        # 完整分到糖果的回合
        k = int(((2 * candies + 0.24) ** 0.5 - 0.5) // num_people)
        
        res[0] = (k - 1) * k * num_people // 2 + k
        for i in range(1, len(res)):
            res[i] = res[i-1] + k
        # 不完整分到糖果的回合
        remain = candies - sum(res)
        for i in range(len(res)):
            if remain <= 0:
                return res
            
            cur = k * num_people + i + 1
            res[i] += remain if cur > remain else cur
            remain -= cur

        return res
        
            
