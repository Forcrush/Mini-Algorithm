'''
Author: Puffrora
Date: 2020-10-13 17:31:16
LastModifiedBy: Puffrora
LastEditTime: 2020-10-13 17:57:07
'''


'''
dp(i, j) 表示下标区间是[i, j]范围内的不同的回文子序列个数
如果S[i] == S[j]:
    dp(i, j) = 2 * dp(i+1, j-1) + 2 
    (乘以2是内部的不同回文个数和套上左右边界两个字符后的不同回文个数，加上2是边界上两个相同字符组合起来可以形成长度是1和长度是2的两个不同的回文)

如果S[i] != S[j]:
    左右两个不同的边界字符不可能同时参与到回文组合中
    dp(i, j) = dp(i+1, j) + dp(i, j-1) - dp(i+1, j-1)

在S[i] == S[j]情况下，还有重复的子串没有摘掉

考虑下面这种情况
acbacba
除了左右边界上的a会形成一个子串a外，中间的cbacb也会形成一个回文子串a, 这个会重复算一次，需要摘掉一个重复的

如果中间有多个a，那情况就比较麻烦
acbcbadddaeeeeacba
中间有三个跟左右边界字符重复的a
    addda 形成的不同子串中会有根最外层两个a包住的回文子串重复
    aeeeea 形成的不同子串中会有根最外层两个a包住的回文子串重复
    adddaeeeea 形成的不同子串中还是会有根最外层两个a包住的回文子串重复
貌似很复杂，但是总体来看，其实形成了冲突的就是adddaeeeea这个区段产生的左右都是a的回文子串

假设最外层的a在i, j两个位置上
中间出现多个a， 分别在k1, k2, k3...kx位置上
dp(i, j) = 2 * dp(i+1, j-1) + 2 -  dp(k1+1, kx-1) - 2

'''
class Solution:
    def countPalindromicSubsequences(self, S):
        n = len(S)
        dp = [[1 for _ in range(n)] for _ in range(n)]

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if S[i] == S[j]:
                    if j == i + 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 2 * dp[i+1][j-1] + 2
                        k1, k2 = -1, -1
                        for k in range(i+1, j):
                            if S[k] == S[i]:
                                k1 = k
                                break
                        for k in range(j-1, i, -1):
                            if S[k] == S[i]:
                                k2 = k
                                break
                        
                        if k1 != -1:
                            if k1 == k2:
                                dp[i][j] -= 1
                            else:
                                if k2 == k1 + 1:
                                    dp[i][j] -= 2
                                else:
                                    dp[i][j] -= dp[k1+1][k2-1] + 2
                        
                else:
                    if j == i + 1:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
    
                dp[i][j] %= 1000000007

        return dp[0][n-1]