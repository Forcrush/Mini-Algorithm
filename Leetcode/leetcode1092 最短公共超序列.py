'''
Author: Puffrora
Date: 2020-12-24 19:17:26
LastModifiedBy: Puffrora
LastEditTime: 2020-12-24 20:55:48
'''


# @ Method1 直接求最短公共超序列
class Solution:
    def shortestCommonSupersequence(self, str1, str2):

        dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

        # . 寻找最短公共超序列长度
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0: dp[i][j] = j
                elif j == 0: dp[i][j] = i
                elif str2[i-1] == str1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

        # . 逆向寻找最短公共超序列
        scs = ''
        i, j = len(str2), len(str1)
        while i > 0 and j > 0:
            if str2[i-1] == str1[j-1]:
                scs += str2[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] < dp[i][j-1]:
                    scs += str2[i-1]
                    i -= 1
                else:
                    scs += str1[j-1]
                    j -= 1
        # 剩下的字符
        while i > 0:
            scs += str2[i-1]
            i -= 1
        while j > 0:
            scs += str1[j-1]
            j -= 1
            
        return scs[::-1]


# @ Method2 先求出最长公共子列再拼接
class Solution2:
    def shortestCommonSupersequence(self, str1, str2):

        dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

        # . 寻找最长公共子列长度
        lcs_len = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if str2[i-1] == str1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                lcs_len = max(lcs_len, dp[i][j])
        
        # . 逆向寻找最长公共子列
        lcs = ''
        i, j = len(str2), len(str1)
        while i > 0 and j > 0:
            if str2[i-1] == str1[j-1]:
                lcs += str2[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                else:
                    j -= 1
        lcs = lcs[::-1]

        # . 拼接成最短公共超序列
        p1, p2, lcs_pos = 0, 0, 0
        res = ''
        while p1 < len(str1) or p2 < len(str2):
            if lcs_pos == len(lcs):
                res += str1[p1:] + str2[p2:]
                break
            while str1[p1] != lcs[lcs_pos]:
                res += str1[p1]
                p1 += 1 
            while str2[p2] != lcs[lcs_pos]:
                res += str2[p2]
                p2 += 1
            res += lcs[lcs_pos]
            p1 += 1
            p2 += 1
            lcs_pos += 1

        return res
