'''
Author: Puffrora
Date: 2020-10-13 08:17:03
LastModifiedBy: Puffrora
LastEditTime: 2020-10-13 08:21:21
'''


class Solution:
    def longestPalindromeSubseq(self, s):

        def largest_common_subsequence(a, b):
            dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
            res = 0
            for i in range(1, len(a)+1):
                for j in range(1, len(b)+1):
                    if a[i-1] == b[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    res = max(res, dp[i][j])
            return res
            
        return largest_common_subsequence(s, s[::-1])