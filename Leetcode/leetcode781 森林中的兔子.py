'''
Author: Puffrora
Date: 2020-10-18 23:03:29
LastModifiedBy: Puffrora
LastEditTime: 2020-10-18 23:15:57
'''


class Solution:
    def numRabbits(self, answers):

        dic = {}
        res = 0
        for num in answers:
            dic[num] = dic.get(num, 0) + 1
        for k, v in dic.items():
            if v % (k + 1) == 0:
                res += v
            else:
                res += v // (k + 1) * (k + 1) + (k + 1)
        
        return res
