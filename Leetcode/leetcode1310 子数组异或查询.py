'''
Author: Puffrora
Date: 2020-12-09 15:47:42
LastModifiedBy: Puffrora
LastEditTime: 2020-12-09 16:19:19
'''


class Solution:
    def xorQueries(self, arr, queries):

        prefix = [0] * (len(arr) + 1)
        for i in range(1, len(arr)+1):
            prefix[i] = prefix[i-1] ^ arr[i-1]
        
        res = []
        for l, r in queries:
            res.append(prefix[l] ^ prefix[r+1])
            
        return res

