'''
Author: Puffrora
Date: 2020-10-13 07:42:14
LastModifiedBy: Puffrora
LastEditTime: 2020-10-13 07:51:13
'''


class Solution:
    def deleteAndEarn(self, nums):

        if not nums: return 0
        
        max_val = max(nums)
        dp = [0] * (max_val + 1)

        for n in nums:
            dp[n] += 1
        dp[1] = 1 * dp[1]

        res = dp[1]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + i * dp[i])
            res = max(res, dp[i])
        
        return res
