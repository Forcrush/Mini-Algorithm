'''
Author: Puffrora
Date: 2020-10-21 23:58:39
LastModifiedBy: Puffrora
LastEditTime: 2020-10-22 00:01:31
'''


class Solution:
    def findPairs(self, nums, k):
        if k < 0: return 0
        seen, diff = set(), set()
        for n in nums:
            if n - k in seen:
                # ! 对于每个 k-diff 对， 只记录较小那个数
                diff.add(n-k)
            if n + k in seen:
                # ! 对于每个 k-diff 对， 只记录较小那个数
                diff.add(n)
            seen.add(n)
            
        return len(diff)